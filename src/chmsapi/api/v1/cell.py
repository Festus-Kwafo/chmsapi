from fastapi import APIRouter


router = APIRouter()


@router.post("/register")
async def cell_register():
    pass