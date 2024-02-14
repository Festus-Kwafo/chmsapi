from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CreateCellSchema(BaseModel):
    name: Optional[str]
    location: Optional[str]
    leader_id: Optional[str]
    constituency_id: Optional[str]
    date_started: Optional[datetime]

    class Config:
        from_attributes = True
        populate_by_name = True


class CellSchema(CreateCellSchema):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True


class UpdateCellSchema(CreateCellSchema):
    class Config:
        from_attributes = True
        populate_by_name = True
