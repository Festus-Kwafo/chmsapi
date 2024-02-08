from fastapi import APIRouter

from src.chmsapi.config.settings import settings

v1 = APIRouter(prefix=settings.API_V1_STR)
