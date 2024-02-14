from src.chmsapi.schemas.member_schema import CreateMember
from src.chmsapi.config.db import async_db_session
from src.chmsapi.handlers.member_handler import CRUDMember
from src.chmsapi.models.member import Member
from src.chmsapi.common.exception import errors
from fastapi import HTTPException, status

class MemberService:
    @staticmethod
    async def register(obj: CreateMember):
        async with async_db_session.begin() as db:
            member = CRUDMember()
            await member.create_member(obj, db)

    @staticmethod
    async def get_all() -> list:
        async with async_db_session.begin() as db:
            return await CRUDMember().get_all_members(db)


    @staticmethod
    async def get_member_by_id(member_id: str) -> Member:
        async with async_db_session.begin() as db:
            results = await CRUDMember().get_by_id_member(db, member_id)
            if results == None:
                raise errors.HTTPError(code=status.HTTP_404_NOT_FOUND)
            else:
                return results

