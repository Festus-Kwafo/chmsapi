from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.chmsapi.models.base import Base
from src.chmsapi.models.base import id_key


class CellConstituency(Base):
    __tablename__ = "cell_constituency"
    id: Mapped[id_key] = mapped_column(init=False)
    cell_id: Mapped[str] = mapped_column(ForeignKey("cell.id"), default=None)
    constituency_id: Mapped[str] = mapped_column(ForeignKey("constituency.id"), unique=True, default=None)


