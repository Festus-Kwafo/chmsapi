from datetime import datetime

from sqlalchemy import Column, String, DateTime, ForeignKey, ForeignKeyConstraint
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.chmsapi.models.base import Base
from src.chmsapi.models.base import Gender, MaritalStatus, EducationLevel, MembershipStatus, LeadershipRole
from src.chmsapi.models.base import id_key
from typing import Optional, List
from src.chmsapi.models.members_departments import members_departments


class Member(Base):
    __tablename__ = "member"

    id: Mapped[id_key] = mapped_column(init=False)
    first_name: Mapped[str] = mapped_column(String(50), default=None, index=True, comment="First Name")
    last_name: Mapped[str] = mapped_column(String(50), default=None, index=True, comment="Last Name")
    email: Mapped[str] = mapped_column(String(50), default=None, unique=True, index=True, comment='email address')
    dob: Mapped[datetime] = mapped_column(DateTime, default=None)
    phone_number: Mapped[str | None] = mapped_column(String(11), default=None, comment='Phone number')
    gender: Mapped[Gender] = Column(Gender, nullable=False)
    nationality: Mapped[str] = mapped_column(String(50), default=None, comment=" Nationality")
    marital_status: Mapped[MaritalStatus] = Column(MaritalStatus, nullable=False, default="MALE")
    address: Mapped[str | None] = mapped_column(LONGTEXT, default=None, comment='Address')
    gps_address: Mapped[str | None] = mapped_column(String(50), default=None, comment="Ghana Post Address")
    educational_level: Mapped[EducationLevel] = Column(EducationLevel, nullable=False)
    membership_status: Mapped[MembershipStatus] = Column(MembershipStatus, nullable=False)
    leadership_role: Mapped[LeadershipRole] = Column(LeadershipRole, nullable=False, comment="Leadership role in the "
                                                                                             "church")
    date_joined: Mapped[datetime] = mapped_column(DateTime, default=None)

    department_id: Mapped[str] = mapped_column(ForeignKey("department.id"), default=None, nullable=True)
    cell_id: Mapped[str] = mapped_column(ForeignKey("cell.id", ondelete="CASCADE"), default=None, nullable=True)

    departments: Mapped[List["Department"]] = relationship(secondary=members_departments,
                                                             back_populates="members", default_factory=list)

    cell: Mapped["Cell"] = relationship("Cell", back_populates="members", default=None)
