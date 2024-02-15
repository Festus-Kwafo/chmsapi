from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from src.chmsapi.common.enums import MembershipStatusEnum, MaritalStatusEnum, LeadershipRoleEnum, EducationLevelEnum, \
    GenderEnum


class CreateMember(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    dob: Optional[datetime]
    phone_number: Optional[str]
    gender: GenderEnum
    nationality: Optional[str]
    marital_status: MaritalStatusEnum
    address: Optional[str]
    gps_address: Optional[str]
    educational_level: EducationLevelEnum
    membership_status: MembershipStatusEnum
    leadership_role: LeadershipRoleEnum
    date_joined: Optional[datetime]

    class Config:
        from_attributes = True


class MemberSchema(CreateMember):
    id: Optional[str]

    class Config:
        from_attributes = True


class UpdateMemberSchema(CreateMember):
    cell_id: Optional[str]
    department_id: Optional[str]

    class Config:
        from_attributes = True
        populate_by_name = True
