from peewee import CharField, DateTimeField, DateField, DecimalField
from datetime import datetime

from backend.app.database.models.base_model import BaseModel

class Product(BaseModel):
    name = CharField()    
    price = DecimalField(max_digits=10, decimal_places=2)
    expiration = DateField(null=True)
    price_brl = DecimalField(max_digits=10, decimal_places=2)
    price_cnh = DecimalField(max_digits=10, decimal_places=2)
    price_mxn = DecimalField(max_digits=10, decimal_places=2)
    price_pln = DecimalField(max_digits=10, decimal_places=2)
    price_jpy = DecimalField(max_digits=10, decimal_places=2)
    created_at = DateTimeField(default=datetime.now)
