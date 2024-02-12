from datetime import datetime

from sqlalchemy import String, DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.chmsapi.models.attendance import Attendance
from src.chmsapi.models.base import Base
from src.chmsapi.models.base import id_key


class AttendanceSettings(Base):
    __tablename__ = "attendance_type"
    id: Mapped[id_key] = mapped_column(init=False)
    service_name: Mapped[str] = mapped_column(String(50), default=None)
    start_time: Mapped[datetime] = mapped_column(DATETIME, default=None)
    end_time: Mapped[datetime] = mapped_column(DATETIME, default=None)

    attendance: Mapped[list[Attendance]] = relationship(default=None)
