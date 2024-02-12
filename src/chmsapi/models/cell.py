from datetime import datetime

from sqlalchemy import String, DATETIME, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.chmsapi.models.base import Base
from src.chmsapi.models.base import id_key
from src.chmsapi.models.member import Member


class Cell(Base):
    __tablename__ = "cell"

    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(String(100), default=None)
    location: Mapped[str] = mapped_column(String(100), default=None)
    leader_id: Mapped[str] = mapped_column(ForeignKey("member.id"))
    constituency_id: Mapped[str] = mapped_column(ForeignKey("constituency.id"))
    date_started: Mapped[datetime] = mapped_column(DATETIME, default=None)

    members: Mapped[list[Member]] = relationship()
