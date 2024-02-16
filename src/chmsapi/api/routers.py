from fastapi import APIRouter

from src.chmsapi.api.v1.cell import router as cell_router
from src.chmsapi.api.v1.constituency import router as constituency_router
from src.chmsapi.api.v1.members import router as member_router
from src.chmsapi.config.settings import settings

v1 = APIRouter(prefix=settings.API_V1_STR)

v1.include_router(member_router, prefix='/member', tags=["Membership"])
v1.include_router(cell_router, prefix='/cell', tags=["Cell"])
v1.include_router(constituency_router, prefix='/constituency', tags=["Constituency"])
