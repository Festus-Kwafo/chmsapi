from fastapi import APIRouter
from src.chmsapi.schemas.member_schema import CreateMember, MemberSchema
from src.chmsapi.handlers.member_handler import CrudMember
from src.chmsapi.services.member_service import MemberService

router = APIRouter()


@router.post("/register", summary="Membership Registration")
async def member_register(request: CreateMember):
    return await MemberService.register(request)
