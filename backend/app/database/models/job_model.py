from peewee import CharField, IntegerField

from backend.app.database.models.base_model import BaseModel

class Job(BaseModel):
    id = CharField(primary_key=True)
    total = IntegerField(default=0)
    inserted = IntegerField(default=0)
