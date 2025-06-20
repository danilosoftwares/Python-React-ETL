from peewee import Model
from backend.app.database.connection import db

class BaseModel(Model):
    class Meta:
        database = db
