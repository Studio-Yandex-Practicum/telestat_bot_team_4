from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.groups import Groups


class CRUDGroups:
    def __init__(self, model):
        self.model = model

    async def create(
        self,
        session: AsyncSession,
        id: int,
        group_name: str,
        group_id: str,
        is_choosed: bool,
    ):
        group = self.model(
            id=id,
            group_name=group_name,
            group_id=group_id,
            is_choosed=is_choosed,
        )
        session.add(group)
        await session.commit()
        await session.refresh(group)
        return group

    async def get(self, group_id: str, session: AsyncSession):
        return (
            await session.execute(select(Groups).filter(Groups.group_id == group_id))
            .scalars()
            .first()
        )

    async def get_all(self, session: AsyncSession):
        return await session.execute(select(Groups)).scalars().all()

    async def remove(
        self,
        group_obj: Groups,
        session: AsyncSession,
    ):
        await session.delete(group_obj)
        await session.commit()
        return group_obj


groups_crud = CRUDGroups(Groups)
