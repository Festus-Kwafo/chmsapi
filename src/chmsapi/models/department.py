from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.chmsapi.models.base import Base
from src.chmsapi.models.base import id_key
from typing import Optional, List
from src.chmsapi.models.members_departments import members_departments


class Department(Base):
    __tablename__ = "department"

    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(String(100), default=None)
    leader: Mapped[str] = mapped_column(ForeignKey("member.id"), default=None)

    members: Mapped[List["Member"]] = relationship(secondary=members_departments,
                                                             back_populates="departments", default_factory=list)
