from backend.app.services.index_service import health_check, read_root

async def get_root():
    return read_root

async def get_health_check():
    return health_check