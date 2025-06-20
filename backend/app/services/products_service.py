import asyncio
import io
import json
import math
from typing import Optional
from aio_pika import IncomingMessage, Message
import pandas as pd
from datetime import date, datetime
from peewee import chunked
from backend.app.database.models.job_model import Job
from backend.app.database.repository.job_repository import create_job, update_job_increase, update_job_total
from backend.app.database.repository.product_repository import get_products, product_bulk
from backend.app.services.exchange_service import fetch_exchange_rates
from decimal import Decimal
from backend.app.messages.connection import setup_rabbit

def safe_float(val):
    if val is None:
        return 0.0
    try:
        f = float(val)
        return f if math.isfinite(f) else 0.0
    except:
        return 0.0

def serialize_product(product):
    return {
        "id": product["id"],
        "name": product["name"],
        "price": safe_float(product["price"]),
        "expiration": product["expiration"].isoformat() if product["expiration"] else None,
        "price_brl": safe_float(product["price_brl"]),
        "price_cnh": safe_float(product["price_cnh"]),
        "price_mxn": safe_float(product["price_mxn"]),
        "price_pln": safe_float(product["price_pln"]),
        "price_jpy": safe_float(product["price_jpy"]),
    }

async def read_all_product(
    skip: int = 0,
    limit: int = 10,
    name: Optional[str] = None,
    price: Optional[Decimal] = None,
    expiration: Optional[str] = None,
    sort: Optional[str] = None
):    
    preview = await get_products(skip=skip,limit=limit, name=name, price=price, expiration=expiration, sort=sort)
    sortType = not ("-" in sort)
    result = { "data": [serialize_product(prod) for prod in preview["data"]] , "total": preview["total"], "sort": { "field": sort.replace("-", ""), "increasing": sortType } }
    return result   

async def send_to_rabbitmq(job_id, products_batch):
    _, channel, _, topic = await setup_rabbit()

    message_data = {
        "job_id": job_id,
        "products": products_batch 
    }

    message = Message(
        body=json.dumps(message_data, default=str).encode(),
        content_type="application/json"
    )

    await channel.default_exchange.publish(message, routing_key=topic)    

def count_lines(contents):    
    text = contents.decode("utf-8")
    lines = text.strip().split("\n")
    total_lines = len(lines) - 1
    return total_lines       

async def upload_file_csv(job_id, contents):    
    job = {"id": job_id,"total": count_lines(contents),"inserted": 0}
    await create_job(job)
    rates = await fetch_exchange_rates()       
    await process_csv(job_id, contents, rates)      
    print('upload complete')   

async def process_csv(job_id, contents, rates):    
    diff = 0
    for chunk in pd.read_csv(io.StringIO(contents.decode('utf-8')), sep=";", chunksize=10000): 
        products_to_create = []

        def process_row(row):
            try:
                price = float(str(row["price"]).replace("$", "").strip())
            except Exception:
                price = 0.0

            try:
                expiration = datetime.strptime(str(row['expiration']), "%m/%d/%Y").date()
                expiration = expiration.strftime('%Y-%m-%d')
            except Exception:
                expiration = None

            name = row['name']
            if not name or str(name).lower() == "nan":
                name = ""

            if str(price).lower() == "nan":
                price = 0

            if not name or price == 0 or not expiration:
                return None                

            return {
                "name": name,
                "price": price,
                "expiration": expiration,
                "price_brl": price * rates.get('brl', 0),
                "price_cnh": price * rates.get('cnh', 0),
                "price_mxn": price * rates.get('mxn', 0),
                "price_pln": price * rates.get('pln', 0),
                "price_jpy": price * rates.get('jpy', 0),
            }

        all = chunk.apply(process_row, axis=1).tolist()
        products_to_create = list(filter(None, all))
        diff = diff + (len(all) - len(products_to_create))

        await send_to_rabbitmq(job_id, products_to_create)

        print('send message block')   

    await update_job_total(job_id, diff)       

async def consuming_products(message: IncomingMessage):
    async with message.process():  
        data = json.loads(message.body)
        if "products" in data:
            await product_bulk(data["products"])            
            await update_job_increase(data["job_id"],len(data["products"]))
            print('get message block by job['+ data["job_id"] + ']', flush=True)            
        else:
            print('not products')