from aiogram.filters import BaseFilter
from aiogram.types import Message
from app.crud.admin import admin_crud
from sqlalchemy.ext.asyncio import AsyncSession


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message, session: AsyncSession) -> bool:
        admin_list = await admin_crud.get_all(session=session)
        admin_id_list = [admin.user_id for admin in admin_list]
        return message.from_user.id in admin_id_list
