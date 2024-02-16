from sqlalchemy import String, ForeignKey, Column, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.chmsapi.models.base import Base, MappedBase
from src.chmsapi.models.base import id_key
from src.chmsapi.models.member import Member
from typing import List


class Department(Base):
    __tablename__ = "department"

    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(String(100), default=None)
    leader: Mapped[str] = mapped_column(ForeignKey("member.id"), default=None)

