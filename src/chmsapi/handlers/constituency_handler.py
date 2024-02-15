from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy import update
from fastapi_pagination import paginate
from src.chmsapi.models.constituency import Constituency
from src.chmsapi.schemas.constituency_schema import CreateConstituencySchema, UpdateConstituencySchema


class CRUDConstituency:
    @staticmethod
    async def create_constituency(constituency_schema: CreateConstituencySchema, db: AsyncSession):
        new_constituency = Constituency(**vars(constituency_schema))
        db.add(new_constituency)
        await db.flush()

    @staticmethod
    async def get_all_constituencies(db: AsyncSession) -> List[Constituency]:
        q = await db.execute(select(Constituency).order_by(Constituency.id))
        return paginate(q.scalars().all())

    @staticmethod
    async def get_by_id_constituency(db: AsyncSession, constituency_id: str) -> Constituency | None:
        q = await db.execute(select(Constituency).filter(Constituency.id == constituency_id))
        return q.one_or_none()

    @staticmethod
    async def update_by_id_constituency(db: AsyncSession, constituency_id: str, constituency_schema: UpdateConstituencySchema) -> Constituency:
        for var, value in vars(constituency_schema).items():
            setattr(constituency_schema, var, value) if value else None

        q = update(Constituency).where(Constituency.id == constituency_id).values(vars(constituency_schema))
        q.execution_options(synchronize_session="fetch")
        await db.execute(q)
        return await CRUDConstituency.get_by_id_constituency(db, constituency_id)