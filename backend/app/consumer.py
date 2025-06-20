import asyncio
from backend.app.services.products_service import consuming_products
from backend.app.messages.connection import start_consumer, isConsumer

if __name__ == "__main__":
        print('consumer online', flush=True)
        asyncio.run(start_consumer(consuming_products))
