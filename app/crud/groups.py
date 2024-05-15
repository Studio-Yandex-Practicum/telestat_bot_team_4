from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.groups import Groups


class CRUDGroups:
    def __init__(self, model):
        self.model = model

    async def create(
        self,
        session: AsyncSession,
        group_name: str,
        group_id: str,
    ):
        group = self.model(
            group_name=group_name,
            group_id=group_id,
        )
        session.add(group)
        await session.commit()

    async def get(self, session: AsyncSession, group_id: str):
        group = await session.execute(
            select(Groups).filter(Groups.group_id == group_id)
        )
        return group.scalars().first()

    async def get_all(
        self,
        session: AsyncSession,
    ):
        all_groups = await session.execute(select(Groups))
        groups_list = all_groups.scalars().all()
        return groups_list

    async def remove(
        self,
        session: AsyncSession,
        group_obj: Groups,
    ):
        await session.delete(group_obj)
        await session.commit()


groups_crud = CRUDGroups(Groups)
