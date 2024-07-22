from fastapi import APIRouter

from api.endpoints import auth, predict



api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(predict.router)
