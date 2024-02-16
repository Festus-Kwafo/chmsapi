from datetime import datetime

from sqlalchemy import String, DATETIME, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.chmsapi.models.base import Base
from src.chmsapi.models.base import id_key
from src.chmsapi.models.cell import Cell

from typing import List


class CellLeaders(Base):
    __tablename__ = "cell_leaders"
    id: Mapped[id_key] = mapped_column(init=False)
    cell_id: Mapped[str] = mapped_column(String(50), unique=True, default=None)
    leader_id: Mapped[str] = mapped_column(String(50), unique=True, default=None)
