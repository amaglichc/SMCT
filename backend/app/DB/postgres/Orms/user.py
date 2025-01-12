from app.DB.postgres.core import Base
from sqlalchemy.orm import Mapped, mapped_column
from app.Models.user import RoleEnum
from sqlalchemy import text
from uuid import uuid4, UUID

class UserOrm(Base):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(primary_key=True,default=uuid4())
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str | None] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(unique=True,nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False,server_default=text("TIMEZONE('utc',now())"))
    role: Mapped[str] = mapped_column(nullable=False,default=RoleEnum.guest)
    