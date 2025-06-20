import asyncio
from typing import Optional
import uuid
from fastapi import Query, UploadFile, File
from decimal import Decimal

from backend.app.services.products_service import upload_file_csv, read_all_product

async def upload_csv(file: UploadFile = File(...)):
    job_id = str(uuid.uuid4())
    contents = await file.read()
    asyncio.create_task(upload_file_csv(job_id, contents))    
    return {"job":job_id, "message": "Upload and processing complete"}    

async def get_all_product(
    skip: int = Query(0),
    limit: int = Query(10),
    name: Optional[str] = Query(None),
    price: Optional[Decimal] = Query(None),
    expiration: Optional[str] = Query(None),
    sort: Optional[str] = Query("id")
):
    result = await read_all_product(skip, limit, name, price, expiration, sort)
    return result