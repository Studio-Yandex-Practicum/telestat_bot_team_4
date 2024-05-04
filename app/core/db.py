from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker, declared_attr

from .config import settings

Base = declarative_base()


class PreBase(Base):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


engine = create_async_engine(settings.database_url)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
async_session = AsyncSessionLocal()


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
