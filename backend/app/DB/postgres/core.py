from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession
from sqlalchemy import declarative_base
from app.config import settings


engine: AsyncEngine = create_async_engine(url=settings.postgres_url)
session_maker = async_sessionmaker(
    bind=engine, autocommit=False, expire_on_commit=False, autoflush=False
)
Base = declarative_base()


async def get_session() -> AsyncSession:
    async with session_maker() as session:
        try:
            yield session
        finally:
            session.close()