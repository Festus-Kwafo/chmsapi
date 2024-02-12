from datetime import datetime

from sqlalchemy import String, DATETIME, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.chmsapi.models.base import Base
from src.chmsapi.models.base import id_key
from src.chmsapi.models.member import Member


class Attendance(Base):
    id: Mapped[id_key] = mapped_column(init=True)
    member: Mapped[str] = mapped_column(ForeignKey("member.id"))
    attendance_type: Mapped[str] = mapped_column(ForeignKey("attendance_type.id"))
