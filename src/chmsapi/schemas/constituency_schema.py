from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CreateConstituencySchema(BaseModel):
    name: Optional[str]
    location: Optional[str]
    leader_id: Optional[str]
    cell_id: Optional[str]
    date_started: Optional[datetime]

    class Config:
        from_attributes = True
        populate_by_name = True


class ConstituencySchema(CreateConstituencySchema):
    id: str

    class Config:
        from_attributes = True
        populate_by_name = True


class UpdateConstituencySchema(CreateConstituencySchema):
    class Config:
        from_attributes = True
        populate_by_name = True
