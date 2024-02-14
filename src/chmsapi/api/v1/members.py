from fastapi import APIRouter
from src.chmsapi.schemas.member_schema import CreateMember, MemberSchema
from src.chmsapi.services.member_service import MemberService
from fastapi_pagination import Page, LimitOffsetPage, paginate

router = APIRouter()


@router.post("/register", summary="Membership Registration")
async def member_register(request: CreateMember):
    return await MemberService.register(request)


@router.get("/all", summary="All Memberships", response_model=Page[MemberSchema])
async def member_all():
    return await MemberService.get_all()


@router.post("/{member_id}/", summary="Get member by id")
async def member_by_id(member_id: str):
    return await MemberService.get_member_by_id(member_id)
