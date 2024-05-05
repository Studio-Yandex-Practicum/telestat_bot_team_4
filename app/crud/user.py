from datetime import datetime

from sqlalchemy import select, Text, Date
from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User


class CRUDUser():

    def __init__(self, model):
        self.model = model

    async def create(
            self,
            session: AsyncSession,
            id: int,
            user_name: str,
            chat_id: int,
            subscribe_date: Date,
            avatar: Text,  # хранение аватара в base64
            utm_mark: str,
            gender: str,
            country: str,
            description: str
    ):
        user = self.model(
            id=id,
            user_name=user_name,
            chat_id=chat_id,
            subscribe_date=subscribe_date,
            avatar=avatar,
            utm_mark=utm_mark,
            gender=gender,
            country=country,
            description=description
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

    async def get(self, session: AsyncSession, id: int):
        return await session.execute(
            select(User).filter(User.id == id)
            ).scalars().first()

    async def get_all(self, session: AsyncSession):
        return await session.execute(select(User)).scalars().all()


user_crud = CRUDUser(User)