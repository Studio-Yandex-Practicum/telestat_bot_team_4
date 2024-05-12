from core.db import Base
from sqlalchemy import Column, String


class Spreadsheet(Base):

    spreadsheet_link = Column(String)
