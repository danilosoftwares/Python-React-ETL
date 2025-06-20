from backend.app.database.models.job_model import Job
from backend.app.services.products_service import consuming_products
from backend.app.database.connection import db    
from fastapi import APIRouter, FastAPI
from backend.app.database.models import Product
from backend.app.routes.index_route import router as index_router
from backend.app.routes.product_route import router as products_router
from backend.app.routes.job_route import router as job_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.on_event("startup")
async def startup():
    db.connect()
    db.create_tables([Product, Job])
    db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routerAPI = APIRouter(prefix='/api')

routerAPI.include_router(index_router)
routerAPI.include_router(products_router)
routerAPI.include_router(job_router)

app.include_router(routerAPI)


