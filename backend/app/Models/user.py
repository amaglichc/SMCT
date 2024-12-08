from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, EmailStr


class RoleEnum(Enum):
    user = "USER"
    admin = "ADMIN"
    dev = "DEV"
    guest = "GUEST"


class SignUpUser(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    surname: str = Field(min_length=3, max_length=20)
    email: EmailStr = Field(min_length=6, max_length=20)
    password: str = Field(min_length=8, max_length=25)


class SignInUser(BaseModel):
    email: str
    password: str


class User(BaseModel):
    id: str
    name: str
    surname: str
    email: str
    password: str
    created_at: datetime
    role: RoleEnum = RoleEnum.guest
