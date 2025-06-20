from fastapi import APIRouter

from backend.app.controllers.index_controller import get_health_check, get_root

router = APIRouter(tags=['Index'])

router.add_api_route("/", get_root)
router.add_api_route("/health", get_health_check)
