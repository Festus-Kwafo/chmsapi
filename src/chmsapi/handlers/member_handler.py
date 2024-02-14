from sqlalchemy.ext.asyncio import AsyncSession
from src.chmsapi.schemas.member_schema import CreateMember
from src.chmsapi.models.member import Member
from src.chmsapi.config.db import async_db_session
from datetime import datetime


class CRUDMember:
    @staticmethod
    async def create_member(member_schema: CreateMember, db: AsyncSession):
        Member()
        new_member = Member(**vars(member_schema))
        db.add(new_member)


CrudMember = CRUDMember()
