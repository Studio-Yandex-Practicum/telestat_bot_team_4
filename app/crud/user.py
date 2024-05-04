from datetime import datetime

from dateutil.relativedelta import relativedelta
from sqlalchemy import and_, select, Text
from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User


class CRUDUser():

    def __init__(self, model):
        self.model = model

    async def create(
            self,
            session: AsyncSession,
            id: int,
            tg_user_id: int,
            user_name: str,
            chat_id: int,
            avatar: Text,  # хранение аватара в base64
            utm_mark: str,
            gender: str,
            country: str,
            description: str
    ):
        subscribe_date = datetime.now()  # Определяем дату подписки
        user = self.model(
            tg_user_id=tg_user_id,
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

    async def get(self, session: AsyncSession, tg_user_id: int):
        return await session.execute(select(User).filter(User.tg_user_id == tg_user_id)).scalars().first()

    async def get_all(self, session: AsyncSession):
        return await session.execute(select(User)).scalars().all()


user_crud = CRUDUser(User)