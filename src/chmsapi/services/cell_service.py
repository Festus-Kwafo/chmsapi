from fastapi import status

from src.chmsapi.common.exception import errors
from src.chmsapi.config.db import async_db_session
from src.chmsapi.handlers.cell_handler import CRUDCell
from src.chmsapi.models.cell import Cell
from src.chmsapi.schemas.cell_schema import CreateCellSchema, CellSchema, UpdateCellSchema


class CellService:
    @staticmethod
    async def register(obj: CreateCellSchema):
        async with async_db_session.begin() as db:
            cell = CRUDCell()
            await cell.create_cell(obj, db)


    @staticmethod
    async def get_all() -> list:
        async with async_db_session.begin() as db:
            return await CRUDCell().get_all_cells(db)

    @staticmethod
    async def get_cell_by_id(cell_id: str) -> Cell:
        async with async_db_session.begin() as db:
            results = await CRUDCell().get_by_id_cell(db, cell_id)
            if results == None:
                raise errors.HTTPError(code=status.HTTP_404_NOT_FOUND)
            else:
                return results

    @staticmethod
    async def update_cell_by_id(cell_id: str, obj: UpdateCellSchema) -> Cell:
        async with async_db_session.begin() as db:
            results = await CRUDCell().update_by_id_cell(db, cell_id, obj)
            if results == None:
                raise errors.HTTPError(code=status.HTTP_404_NOT_FOUND)
            else:
                return results
