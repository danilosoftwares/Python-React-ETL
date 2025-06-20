from backend.app.database.models.job_model import Job
from backend.app.database.connection import db 

async def create_job(job_data):
    with db.atomic():
        job = Job.create(**job_data)
        return job
    
async def update_job_increase(job_id, increase_value):    
    with db.atomic():
        job = Job.update(inserted=Job.inserted + increase_value).where(Job.id == job_id).execute()        
        return job     
    
async def update_job_total(job_id, total_value):    
    with db.atomic():
        job = Job.update(total=Job.total - total_value).where(Job.id == job_id).execute()        
        return job       
    
async def get_job_by_id(job_id):
    return Job.get_or_none(Job.id == job_id) 