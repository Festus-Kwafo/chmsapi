from fastapi import APIRouter
from fastapi_pagination import Page

from src.chmsapi.schemas.member_schema import CreateMember, MemberSchema, UpdateMemberSchema
from src.chmsapi.services.member_service import MemberService

router = APIRouter()


@router.post("/register", summary="Membership Registration")
async def member_register(request: CreateMember):
    return await MemberService.register(request)


@router.get("/all", summary="All Memberships", response_model=Page[MemberSchema])
async def member_all():
    return await MemberService.get_all()


@router.get("/{member_id}/", summary="Get member by id", response_model=MemberSchema)
async def member_by_id(member_id: str):
    return await MemberService.get_member_by_id(member_id)


@router.put("/{member_id}/", summary="Update member by id", response_model=MemberSchema)
async def member_update_by_id(member_id: str, request: UpdateMemberSchema):
    return await MemberService.update_member_by_id(member_id, request)
