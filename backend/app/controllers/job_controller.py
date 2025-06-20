from fastapi import HTTPException, Query
from backend.app.services.job_service import read_job_by_id

async def get_job_by_id(job_id: str = Query(..., description="Required Job ID")):
    try:
        job = await read_job_by_id(job_id)
        if job is None:
            raise HTTPException(status_code=404, detail="Job not found")
        return {
            "id": job.id,
            "total": job.total,
            "inserted": job.inserted,
            "percent": round((job.inserted / job.total) * 100, 2) if job.total else 0.0
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))