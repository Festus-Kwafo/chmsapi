from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy import select
from src.chmsapi.schemas.member_schema import CreateMember
from src.chmsapi.models.member import Member
from src.chmsapi.config.db import async_db_session
from datetime import datetime
from fastapi_pagination import paginate
from fastapi_pagination.utils import disable_installed_extensions_check
from typing import List

disable_installed_extensions_check()


class CRUDMember:
    @staticmethod
    async def create_member(member_schema: CreateMember, db: AsyncSession):
        new_member = Member(**vars(member_schema))
        db.add(new_member)
        await db.flush()

    @staticmethod
    async def get_all_members(db: AsyncSession) -> List[Member]:
        q = await db.execute(select(Member).order_by(Member.id))
        return paginate(q.scalars().all())

    @staticmethod
    async def get_by_id_member(db: AsyncSession, member_id: str) -> Member | None:
        q = await db.execute(select(Member).filter(Member.id == member_id))
        return q.one_or_none()
