from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker
from app.config import settings


engine: AsyncEngine = AsyncEngine(url=settings.postgres_url)
session_maker = async_sessionmaker(bind=engine)