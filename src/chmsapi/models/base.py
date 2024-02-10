from datetime import datetime, timezone
from typing_extensions import Annotated
from sqlalchemy.orm import MappedAsDataclass, Mapped, DeclarativeBase, mapped_column, declared_attr
from sqlalchemy import String
from uuid import uuid4
from ulid import ULID
from sqlalchemy.dialects.mysql import ENUM as mysql_enum
from src.chmsapi.common.enums import GenderEnum, MaritalStatusEnum, EducationLevelEnum, MembershipStatusEnum, \
    LeadershipRoleEnum


class DateTimeMixin(MappedAsDataclass):
    created_date: Mapped[datetime] = mapped_column(init=False, sort_order=999,
                                                   default_factory=datetime.now(timezone.utc))
    updated_date: Mapped[datetime] = mapped_column(init=False, sort_order=999, onupdate=datetime.now(timezone.utc))


class MappedBase(DeclarativeBase):

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class DataClassBase(MappedAsDataclass, MappedBase):
    __abstract__ = True


class Base(DataClassBase, DateTimeMixin):
    __abstract__ = True


id_key = Annotated[
    int, mapped_column(String(50), primary_key=True, default_factory=ULID.from_datetime(datetime.utcnow()), unique=True)
]

Gender: mysql_enum = mysql_enum(GenderEnum, name="gender", create_constraint=True,
                                metadata=Base.metadata,
                                validate_strings=True)

MaritalStatus: mysql_enum = mysql_enum(MaritalStatusEnum, name="marital_status", create_constraint=True,
                                       metadata=Base.metadata,
                                       validate_strings=True)

EducationLevel: mysql_enum = mysql_enum(EducationLevelEnum, name="educational_level", create_constraint=True,
                                        metadata=Base.metadata,
                                        validate_strings=True)

MembershipStatus: mysql_enum = mysql_enum(MembershipStatusEnum, name="membership_status", create_constraint=True,
                                          metadata=Base.metadata,
                                          validate_strings=True)
LeadershipRole: mysql_enum = mysql_enum(LeadershipRoleEnum, name="leadership_role", create_constraint=True,
                                        metadata=Base.metadata,
                                        validate_strings=True)
