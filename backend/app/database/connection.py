import peewee
import os

DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER', 'user')}:{os.getenv('POSTGRES_PASSWORD', 'password')}"
    f"@{os.getenv('POSTGRES_HOST','localhost')}:{os.getenv('POSTGRES_PORT', '5432')}/{os.getenv('POSTGRES_DATABASE','products_db')}"
)

db = peewee.PostgresqlDatabase(DATABASE_URL, autorollback=True)
