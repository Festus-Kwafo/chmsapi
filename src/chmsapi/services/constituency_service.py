from fastapi import status

from src.chmsapi.common.exception import errors
from src.chmsapi.config.db import async_db_session
from src.chmsapi.handlers.constituency_handler import CRUDConstituency
from src.chmsapi.schemas.constituency_schema import CreateConstituencySchema, UpdateConstituencySchema


class ConstituencyService:
    @staticmethod
    async def register(constituency: CreateConstituencySchema):
        async with async_db_session.begin() as db:
            return await CRUDConstituency.create_constituency(constituency, db)

    @staticmethod
    async def get_all():
        async with async_db_session.begin() as db:
            return await CRUDConstituency.get_all_constituencies(db)

    @staticmethod
    async def get_constituency_by_id(constituency_id: str):
        async with async_db_session.begin() as db:
            results = await CRUDConstituency.get_by_id_constituency(db, constituency_id)
            if results == None:
                raise errors.HTTPError(code=status.HTTP_404_NOT_FOUND)
            else:
                return results

    @staticmethod
    async def update_constituency_by_id(constituency_id: str, constituency: UpdateConstituencySchema):
        async with async_db_session.begin() as db:
            results = await CRUDConstituency.update_by_id_constituency(db, constituency_id, constituency)
            if results == None:
                raise errors.HTTPError(code=status.HTTP_404_NOT_FOUND)
            else:
                return results

    @staticmethod
    async def get_cells_by_id_constituency(constituency_id: str):
        async with async_db_session.begin() as db:
            results = await CRUDConstituency.get_cells_by_constituency_id(db, constituency_id)
            if results == None:
                raise errors.HTTPError(code=status.HTTP_404_NOT_FOUND)
            else:
                return results
