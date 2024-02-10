from enum import Enum


class GenderEnum(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class MaritalStatusEnum(str, Enum):
    SINGLE = " SINGLE"
    MARRIED = "MARRIED"
    DIVORCED = "DIVORCED"


class EducationLevelEnum(str, Enum):
    TERTIARY = "TERTIARY"
    SECONDARY = "SECONDARY"
    PRIMARY = "PRIMARY"


class MembershipStatusEnum(str, Enum):
    MEMBER = "MEMBER"
    LEADER = "LEADER"


class LeadershipRoleEnum(str, Enum):
    DEACON = "DEACON"
    DEACONESS = "DEACONESS"
    SHEPHERD = "SHEPHERD"
    ELDER = "ELDER"
    PASTOR = "PASTOR"
    LADY_PASTOR = "LADY_PASTOR"
    REVEREND = "REVEREND"
