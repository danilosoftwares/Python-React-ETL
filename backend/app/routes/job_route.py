from fastapi import APIRouter

from backend.app.controllers.job_controller import get_job_by_id

router = APIRouter(tags=['Job'],prefix='/jobs')

router.add_api_route("/byId", get_job_by_id)
