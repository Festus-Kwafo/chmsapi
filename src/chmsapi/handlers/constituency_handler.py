from typing import List

from fastapi_pagination import paginate
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from src.chmsapi.common.exception.errors import HTTPError
from src.chmsapi.common.logs import log
from src.chmsapi.models.base import generate_id
from src.chmsapi.models.constituency import Constituency
from src.chmsapi.schemas.constituency_schema import CreateConstituencySchema, UpdateConstituencySchema


class CRUDConstituency:
    @staticmethod
    async def create_constituency(constituency_schema: CreateConstituencySchema, db: AsyncSession):
        log.debug("Inside create_constituency")
        try:
            log.debug("Creating constituency " + str(dict(constituency_schema)))
            new_constituency = Constituency(**vars(constituency_schema))
            new_constituency.id = generate_id()
            db.add(new_constituency)
            await db.flush()
            return new_constituency
        except Exception as e:
            log.error(e)
            raise HTTPError(code=422)

    @staticmethod
    async def get_all_constituencies(db: AsyncSession) -> List[Constituency]:
        log.debug("Inside get_all_constituencies")
        try:
            q = await db.execute(select(Constituency).order_by(Constituency.id))
            log.debug('Getting all constituencies')
            return paginate(q.scalars().all())
        except Exception as e:
            log.error(e)
            raise HTTPError(code=404)

    @staticmethod
    async def get_by_id_constituency(db: AsyncSession, constituency_id: str) -> Constituency | None:
        try:
            q = await db.execute(select(Constituency).filter(Constituency.id == constituency_id))
            return q.one_or_none()
        except Exception as e:
            log.error(e)
            raise HTTPError(code=404)

    @staticmethod
    async def update_by_id_constituency(db: AsyncSession, constituency_id: str,
                                        constituency_schema: UpdateConstituencySchema) -> Constituency:
        log.debug("Inside update_by_id_constituency")
        try:
            for var, value in vars(constituency_schema).items():
                setattr(constituency_schema, var, value) if value else None

            q = update(Constituency).where(Constituency.id == constituency_id).values(vars(constituency_schema))
            q.execution_options(synchronize_session="fetch")
            await db.execute(q)
            log.debug(f'Updating constituency by id {str(constituency_id)} with {str(vars(constituency_schema))}')
            return await CRUDConstituency.get_by_id_constituency(db, constituency_id)
        except Exception as e:
            log.error(e)
            raise HTTPError(code=404)

    @staticmethod
    async def get_cells_by_constituency_id(db: AsyncSession, constituency_id: str) -> List:
        try:
            q = await db.execute(select(Constituency).filter(Constituency.id == constituency_id))
            constituency = q.one_or_none()
            return constituency.cells
        except Exception as e:
            log.error(e)
            raise HTTPError(code=404)
