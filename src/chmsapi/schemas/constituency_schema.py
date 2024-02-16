from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateConstituencySchema(BaseModel):
    name: Optional[str]
    location: Optional[str]
    leader: Optional[str]
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
