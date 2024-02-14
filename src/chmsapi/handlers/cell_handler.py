from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy import update
from fastapi_pagination import paginate
from src.chmsapi.models.cell import Cell
from src.chmsapi.schemas.cell_schema import CreateCellSchema, UpdateCellSchema


class CRUDCell:
    @staticmethod
    async def create_cell(cell_schema: CreateCellSchema, db: AsyncSession):
        new_cell = Cell(**vars(cell_schema))
        db.add(new_cell)
        await db.flush()

    @staticmethod
    async def get_all_cells(db: AsyncSession) -> List[Cell]:
        q = await db.execute(select(Cell).order_by(Cell.id))
        return paginate(q.scalars().all())

    @staticmethod
    async def get_by_id_cell(db: AsyncSession, cell_id: str) -> Cell | None:
        q = await db.execute(select(Cell).filter(Cell.id == cell_id))
        return q.one_or_none()

    @staticmethod
    async def update_by_id_cell(db: AsyncSession, cell_id: str, cell_schema: UpdateCellSchema) -> Cell:
        for var, value in vars(cell_schema).items():
            setattr(cell_schema, var, value) if value else None

        q = update(Cell).where(Cell.id == cell_id).values(vars(cell_schema))
        q.execution_options(synchronize_session="fetch")
        await db.execute(q)
        return await CRUDCell.get_by_id_cell(db, cell_id)
