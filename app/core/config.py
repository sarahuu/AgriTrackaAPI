import pathlib, os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from typing import List


load_dotenv()


ROOT = pathlib.Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    SECRET_KEY:str = os.environ.get('SECRET_KEY')
    ALGORITHM:str = 'HS256'
    BACKEND_CORS_ORIGINS: List[str] = ['*']
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 120
    API_USERNAME:str = os.environ.get('API_USERNAME')
    API_PASSWORD:str = os.environ.get('API_PASSWORD')

    class Config:
        case_sensitive = True

settings = Settings()
print(settings.API_USERNAME)