from sqlalchemy import Date, Text, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User


class CRUDUser:
    def __init__(self, model):
        self.model = model

    async def create(
        self,
        session: AsyncSession,
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

        session.add(user)
        await session.commit()

    async def get(self, session: AsyncSession, id: int):
        obj_user = await session.execute(select(User).filter(User.id == id))
        user = obj_user.scalars().first()
        return user

    async def get_all(
        self,
        session: AsyncSession,
    ):
        all_users = await session.execute(select(User))
        users_list = all_users.scalars().all()
        return users_list


user_crud = CRUDUser(User)
