from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.spreadsheet import Spreadsheet


class CRUDSpreadsheet():

    def __init__(self, model):
        self.model = model

    async def create(
            self,
            session: AsyncSession,
            id: int,
            spreadsheet_link: str,
    ):
        spreadsheet = self.model(
            id=id,
            spreadsheet_link=spreadsheet_link,
        )
        session.add(spreadsheet)
        await session.commit()
        await session.refresh(spreadsheet)
        return spreadsheet

    async def get_by_group(self, session: AsyncSession):
        return await session.execute(
            select(Spreadsheet).filter(Spreadsheet.id == id)
            ).scalars().first()

    async def delete_by_group(self, spreadsheet_obj, session: AsyncSession):
        await session.delete(spreadsheet_obj)
        await session.commit()
        return spreadsheet_obj


admin_crud = CRUDSpreadsheet(Spreadsheet)
