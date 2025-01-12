from sqlalchemy.ext.asyncio import AsyncSession
from app.Models.user import SignUpUser,User
from app.DB.postgres.Orms.user import UserOrm
from security import hash_password

class UserRepository():
    def __init__(self,session: AsyncSession):
        self.session = session
        
    async def create_user(user: SignUpUser) -> User:
        async with self.session as session:
            orm = UserOrm(name=user.name,surname=user.surname,email=user.email,role=user.role,password=hash_password(user.password))
            session.add(orm)
            await session.commit()
            