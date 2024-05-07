from handlers.exceptions import error_admin_is_superuser
from models.admin import Admin
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDAdmin():

    def __init__(self, model):
        self.model = model

    async def create(
            self,
            session: AsyncSession,
            id: int,
            is_superuser: bool,
    ):
        admin = self.model(
            id=id,
            is_superuser=is_superuser,
        )
        session.add(admin)
        await session.commit()
        await session.refresh(admin)
        return admin

    async def get_all(self, session: AsyncSession):
        return await session.execute(select(Admin)).scalars().all()

    async def remove(self, admin_obj, session: AsyncSession):
        if admin_obj.is_superuser is True:
            error_admin_is_superuser()
        await session.delete(admin_obj)
        await session.commit()
        return admin_obj


admin_crud = CRUDAdmin(Admin)
