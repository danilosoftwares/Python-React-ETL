import asyncio
from datetime import datetime
from backend.app.database.models import Product
from backend.app.database.connection import db 
from typing import Optional
from decimal import Decimal

async def create_product(product_data):
    with db.atomic():
        product = Product.create(**product_data)
        return product
    
async def product_bulk(product_data):
    try:
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, lambda: Product.insert_many(product_data).execute())        
    except Exception as e:
        print("error on save products")

def get_filtered_query(name=None, price=None, expiration=None, order_by=None):
    query = Product.select()
    if name:
        query = query.where(Product.name.contains(name))
    if price is not None:
        query = query.where(Product.price == price)
    if expiration:
        try:
            expiration_date = datetime.strptime(expiration, "%Y-%m-%d").date()
            query = query.where(Product.expiration == expiration_date)
        except ValueError:
            raise ValueError("format invalid. Use YYYY-MM-DD.")
        
    if order_by:
        order_field = order_by.lstrip("-")
        desc = order_by.startswith("-")

        if not hasattr(Product, order_field):
            raise ValueError(f"Invalid field for ordering: {order_field}")

        column = getattr(Product, order_field)
        query = query.order_by(column.desc() if desc else column.asc())        
    return query

async def get_products(
    skip: int = 0,
    limit: int = 10,
    name: Optional[str] = None,
    price: Optional[Decimal] = None,
    expiration: Optional[str] = None,
    sort: Optional[str] = None
):
    count = get_filtered_query(name, price, expiration, sort).count()
    query = get_filtered_query(name, price, expiration, sort).offset(skip*limit).limit(limit)
    result = { "data": list(query.dicts()), "total":count }
    return result
