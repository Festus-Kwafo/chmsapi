from fastapi import APIRouter
from fastapi_pagination import Page

from src.chmsapi.schemas.cell_schema import CreateCellSchema, CellSchema, UpdateCellSchema
from src.chmsapi.services.cell_service import CellService

router = APIRouter()


@router.post("/register", summary="Cell Registration", response_model=CellSchema)
async def cell_register(request: CreateCellSchema):
    return await CellService.register(request)


@router.get("/all", summary="All Cells", response_model=Page[CellSchema])
async def cell_all():
    return await CellService.get_all()


@router.get("/{cell_id}/", summary="Get cell by id", response_model=CellSchema)
async def cell_by_id(cell_id: str):
    return await CellService.get_cell_by_id(cell_id)


@router.put("/{cell_id}/", summary="Update cell by id", response_model=CellSchema)
async def cell_update_by_id(cell_id: str, request: UpdateCellSchema):
    return await CellService.update_cell_by_id(cell_id, request)
