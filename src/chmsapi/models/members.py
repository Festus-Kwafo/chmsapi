from src.chmsapi.config.db import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.chmsapi.models.base import id_key
from datetime import datetime

class Members(Base):
    __tablename__ = "members"
    id: Mapped[id_key] = mapped_column(init=False)
    first_name: Mapped[str] = mapped_column(String(50), default=None, comment="First Name")
    last_name: Mapped[str] = mapped_column(String(50), default=None, comment="Last Name")
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True, comment='email address')
    dob = Mapped[datetime] = mapped_column()
    phone: Mapped[str | None] = mapped_column(String(11), default=None, comment='Phone number')
