from fastapi import APIRouter

from backend.app.controllers.products_controller import get_all_product, upload_csv

router = APIRouter(tags=['Products'],prefix='/products')

router.add_api_route("/All", get_all_product, methods=["GET"])
router.add_api_route("/Upload", upload_csv, methods=["POST"])
