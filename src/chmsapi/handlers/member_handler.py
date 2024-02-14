from typing import List

from fastapi_pagination import paginate
from fastapi_pagination.utils import disable_installed_extensions_check
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from src.chmsapi.models.member import Member
from src.chmsapi.schemas.member_schema import CreateMember, UpdateMemberSchema

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

    @staticmethod
    async def update_by_id_member(db: AsyncSession, member_id: str, member_schema: UpdateMemberSchema) -> Member:
        for var, value in vars(member_schema).items():
            setattr(member_schema, var, value) if value else None
        q = update(Member).where(Member.id == member_id).values(vars(member_schema))
        q.execution_options(synchronize_session="fetch")
        await db.execute(q)
        return await CRUDMember.get_by_id_member(db, member_id)
