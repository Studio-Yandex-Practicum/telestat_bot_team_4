from core.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class Spreadsheet(Base):

    spreadsheet_link = Column(String)
    group_id = Column(Integer, ForeignKey('group.id'))
