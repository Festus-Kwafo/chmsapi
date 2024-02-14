from src.chmsapi.schemas.member_schema import CreateMember
from src.chmsapi.config.db import async_db_session
from src.chmsapi.handlers.member_handler import CRUDMember


class MemberService:
    @staticmethod
    async def register(obj: CreateMember):
        async with async_db_session.begin() as db:
            await CRUDMember.create_member(obj, db)
