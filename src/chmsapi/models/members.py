from datetime import datetime

from sqlalchemy import Column, String, DATETIME
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column

from src.chmsapi.models.base import Base
from src.chmsapi.models.base import Gender, MaritalStatus, EducationLevel, MembershipStatus, LeadershipRole
from src.chmsapi.models.base import id_key


class Members(Base):
    __tablename__ = "members"

    id: Mapped[id_key] = mapped_column(init=False)
    first_name: Mapped[str] = mapped_column(String(50), default=None, comment="First Name")
    last_name: Mapped[str] = mapped_column(String(50), default=None, comment="Last Name")
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True, comment='email address')
    dob = Mapped[datetime] = mapped_column(DATETIME, default=None)
    phone_number: Mapped[str | None] = mapped_column(String(11), default=None, comment='Phone number')
    gender: Mapped[Gender] = Column(Gender, nullable=False)
    nationality: Mapped[str] = mapped_column(String(50), index=True, comment=" Nationality")
    marital_status: Mapped[MaritalStatus] = Column(MaritalStatus, nullable=False, default="MALE")
    address: Mapped[str | None] = mapped_column(LONGTEXT, default=None, comment='Address')
    gps_address: Mapped[str | None] = mapped_column(String(50), default=None, comment="Ghana Post Address")
    educational_level: Mapped[EducationLevel] = Column(EducationLevel, nullable=False)
    membership_status: Mapped[MembershipStatus] = Column(MembershipStatus, nullable=False)
    leadership_role: Mapped[LeadershipRole] = Column(LeadershipRole, nullable=False, comment="Leadership role in the "
                                                                                             "church")
    date_joined: Mapped[datetime] = mapped_column(DATETIME, default=None)
