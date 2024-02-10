from src.chmsapi.models.base import Base
from sqlalchemy import Column, String, DATETIME, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.chmsapi.models.base import id_key
from datetime import datetime
from src.chmsapi.models.base import Gender, MaritalStatus, EducationLevel, MembershipStatus, LeadershipRole
from sqlalchemy.dialects.mysql import LONGTEXT


class Cell(Base):
    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(String(100), default=None)
    location: Mapped[str] = mapped_column(String(100), default=None)
    leader: Mapped[str] = mapped_column(ForeignKey("member.id"))


