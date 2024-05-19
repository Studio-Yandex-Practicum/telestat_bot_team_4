from sqlalchemy import Column, ForeignKey, Integer, String

from core.db import Base


class Spreadsheet(Base):

    spreadsheet_link = Column(String)
    group_id = Column(Integer, ForeignKey('group.id'))
