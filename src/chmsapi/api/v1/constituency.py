from fastapi import APIRouter
from fastapi_pagination import Page

from src.chmsapi.services.constituency_service import ConstituencyService
from src.chmsapi.schemas.constituency_schema import CreateConstituencySchema, UpdateConstituencySchema, ConstituencySchema

router = APIRouter()

@router.post("/register", summary="Constituency Registration")
async def constituency_register(request: CreateConstituencySchema):
    return await ConstituencyService.register(request)


@router.get("/all", summary="All Constituencies", response_model=Page[ConstituencySchema])
async def constituency_all():
    return await ConstituencyService.get_all()


@router.get("/{constituency_id}/", summary="Get constituency by id", response_model=ConstituencySchema)
async def constituency_by_id(constituency_id: str):
    return await ConstituencyService.get_constituency_by_id(constituency_id)


@router.put("/{constituency_id}/", summary="Update constituency by id", response_model=ConstituencySchema)
async def constituency_update_by_id(constituency_id: str, request: UpdateConstituencySchema):
    return await ConstituencyService.update_constituency_by_id(constituency_id, request)
