
from backend.app.database.repository.job_repository import get_job_by_id

async def read_job_by_id(job_id):
    return await get_job_by_id(job_id)