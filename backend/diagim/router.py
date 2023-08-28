from ninja import Router
from diagim.api import router

diagim_router = Router()
diagim_router.add_router('/', router, tags=["Diagim"])