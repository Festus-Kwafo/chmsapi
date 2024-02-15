from pydantic import BaseModel
from datetime import datetime
class LoginLogBase(BaseModel):
    user_uuid: str
    username: str
    status: int
    ip: str
    country: str | None
    region: str | None
    city: str | None
    user_agent: str
    browser: str | None
    os: str | None
    device: str | None
    msg: str
    login_time: datetime