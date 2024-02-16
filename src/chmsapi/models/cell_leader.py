from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.chmsapi.models.base import Base
from src.chmsapi.models.base import id_key


class CellLeaders(Base):
    __tablename__ = "cell_leaders"
    id: Mapped[id_key] = mapped_column(init=False)
    cell_id: Mapped[str] = mapped_column(ForeignKey("cell.id"), unique=True, default=None)
    leader_id: Mapped[str] = mapped_column(ForeignKey("member.id"), unique=True, default=None)


