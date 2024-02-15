from pydantic import BaseModel, EmailStr, Field


class Auth(BaseModel):
    email: str
    password: str


class RegisterUser(BaseModel):
    email: EmailStr = Field(..., example='user@example.com')
    password: str
    is_superuser: bool
    is_staff: bool
    is_active: bool



