from datetime import datetime

from sqlalchemy import select, Text, Date
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import AsyncSessionLocal

from app.models.user import User


class CRUDUser:
    def __init__(self, model):
        self.model = model

    async def create(
        self,
        user_id: int,
        first_name: str,
        last_name: str,
        user_name: str,
        chat_id: int,
        subscribe_date: Date,
        avatar: Text,  # хранение аватара в base64
        utm_mark: str,
        gender: str,
        country: str,
        description: str,
    ):
        user = self.model(
            user_id=user_id,
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            chat_id=chat_id,
            subscribe_date=subscribe_date,
            avatar=avatar,
            utm_mark=utm_mark,
            gender=gender,
            country=country,
            description=description,
        )
        async with AsyncSessionLocal() as session:
            session.add(user)
            await session.commit()

    async def get(self, session: AsyncSession, id: int):
        return (
            await session.execute(select(User).filter(User.id == id)).scalars().first()
        )

    async def get_all(
        self,
    ):
        async with AsyncSessionLocal() as session:
            all_users = await session.execute(select(User))
            users_list = all_users.scalars().all()
            return users_list


user_crud = CRUDUser(User)
