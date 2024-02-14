from fastapi import APIRouter

from src.chmsapi.config.settings import settings
from src.chmsapi.api.v1.members import router as member_router

v1 = APIRouter(prefix=settings.API_V1_STR)

v1.include_router(member_router, prefix='/member', tags=["Membership"])
