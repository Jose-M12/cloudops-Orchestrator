from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from .config import settings

engine = create_async_engine(settings.DATABASE_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()

async def get_db():
    async with async_session() as session:
        yield session
