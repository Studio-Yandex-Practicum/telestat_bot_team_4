from app.models.admin import Admin
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import AsyncSessionLocal


class CRUDAdmin:
    def __init__(self, model):
        self.model = model

    async def create(
        self,
        is_superuser: bool,
        user_id: int,
    ):
        admin = self.model(
            is_superuser=is_superuser,
            user_id=user_id,
        )
        async with AsyncSessionLocal() as session:
            session.add(admin)
            await session.commit()

    async def get_all(
        self,
    ) -> list:
        async with AsyncSessionLocal() as session:
            admin_list = await session.execute(select(Admin))
            admins = admin_list.scalars().all()
            return admins

    async def remove(self, admin_obj, session: AsyncSession):
        if not admin_obj.is_superuser:
            await session.delete(admin_obj)
            await session.commit()
            return admin_obj


admin_crud = CRUDAdmin(Admin)
