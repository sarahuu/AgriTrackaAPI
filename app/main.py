from fastapi import FastAPI,APIRouter,Request

from app.api import routers
from pathlib import Path
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware


BASE_PATH = Path(__file__).resolve().parent
root_router = APIRouter()
app = FastAPI(title="AgriTracka")


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins = settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=['*']

    )

@root_router.get("/", status_code=200)
def root(
    request: Request,
) -> dict:
    """
    Root GET
    """
    return {
        'msg':'Welcome to AgriTracka!'
    }

app.include_router(root_router)
app.include_router(routers.api_router, prefix='/api')




if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8001, log_level="debug")