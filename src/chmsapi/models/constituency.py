from datetime import datetime

from sqlalchemy import String, DATETIME, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.chmsapi.models.base import Base
from src.chmsapi.models.base import id_key
from src.chmsapi.models.cell import Cell


class Constituency(Base):
    __tablename__ = "constituency"

    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(String(100), default=None)
    location: Mapped[str] = mapped_column(String(100), default=None)
    #leader: Mapped[str] = mapped_column(ForeignKey("member.id"), default=None)
    date_started: Mapped[datetime] = mapped_column(DATETIME, default=None)
    #cells: Mapped[list[Cell]] = relationship(default=None)
