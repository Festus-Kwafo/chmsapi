from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy import update
from fastapi_pagination import paginate
from src.chmsapi.models.cell import Cell
from src.chmsapi.schemas.cell_schema import CreateCellSchema, UpdateCellSchema
from src.chmsapi.common.logs import log
from src.chmsapi.common.exception.errors import HTTPError


class CRUDCell:
    @staticmethod
    async def create_cell(cell_schema: CreateCellSchema, db: AsyncSession):
        log.debug("Inside create_cell")
        try:
            new_cell = Cell(**vars(cell_schema))
            db.add(new_cell)
            log.debug("Creating cell " + str(dict(cell_schema)))
            await db.flush()
        except Exception as e:
            log.error(e)
            raise HTTPError(code=422)

    @staticmethod
    async def get_all_cells(db: AsyncSession) -> List[Cell]:
        log.debug("Inside get_all_cells")
        try:
            q = await db.execute(select(Cell).order_by(Cell.id))
            return paginate(q.scalars().all())
        except Exception as e:
            log.error(e)
            raise HTTPError(code=404)

    @staticmethod
    async def get_by_id_cell(db: AsyncSession, cell_id: str) -> Cell | None:
        log.debug("Inside get_by_id_cell")
        try:
            q = await db.execute(select(Cell).filter(Cell.id == cell_id))
            return q.one_or_none()
        except Exception as e:
            log.error(e)
            raise HTTPError(code=404)

    @staticmethod
    async def update_by_id_cell(db: AsyncSession, cell_id: str, cell_schema: UpdateCellSchema) -> Cell:
        log.debug("Inside update_by_id_cell")
        try:
            for var, value in vars(cell_schema).items():
                setattr(cell_schema, var, value) if value else None

            q = update(Cell).where(Cell.id == cell_id).values(vars(cell_schema))
            q.execution_options(synchronize_session="fetch")
            await db.execute(q)
            log.debug(f'Updating cell by id {str(cell_id)} with {str(vars(cell_schema))}')
            return await CRUDCell.get_by_id_cell(db, cell_id)
        except Exception as e:
            log.error(e)
            raise HTTPError(code=404)
