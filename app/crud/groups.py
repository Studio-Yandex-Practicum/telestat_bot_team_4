from sqlalchemy import select
from app.core.db import AsyncSessionLocal
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.groups import Groups


class CRUDGroups:
    def __init__(self, model):
        self.model = model

    async def create(
        self,
        group_name: str,
        group_id: str,
    ):
        group = self.model(
            group_name=group_name,
            group_id=group_id,
        )
        async with AsyncSessionLocal() as session:
            session.add(group)
            await session.commit()

    async def get(self, group_id: str):
        async with AsyncSessionLocal() as session:
            group = await session.execute(
                select(Groups).filter(Groups.group_id == group_id)
            )
        return group.scalars().first()

    async def get_all(
        self,
    ):
        async with AsyncSessionLocal() as session:
            all_groups = await session.execute(select(Groups))
            groups_list = all_groups.scalars().all()
        return groups_list

    async def remove(
        self,
        group_obj: Groups,
    ):
        async with AsyncSessionLocal() as session:
            await session.delete(group_obj)
            await session.commit()
        return group_obj


groups_crud = CRUDGroups(Groups)
