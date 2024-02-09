from datetime import datetime
from typing_extensions import Annotated
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column
from sqlalchemy import String
from uuid import uuid4


class DateTimeMixin(MappedAsDataclass):
    created_date: Mapped[datetime] = mapped_column(init=False, )


id_key = Annotated[
    int, mapped_column(String(50), primary_key=True, default_factory=uuid4, unique=True)
]
