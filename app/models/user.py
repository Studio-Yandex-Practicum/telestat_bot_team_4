from datetime import datetime

from core.db import Base
from sqlalchemy import Column, DateTime, Integer, String, Text


class User(Base):
    __tablename__ = 'user'
    
    user_name = Column(String)
    chat_id = Column(Integer)
    subscribe_date = Column(DateTime)
    unsubscribe_date = Column(DateTime, nullable=True)
    avatar = Column(Text, nullable=True)
    utm_mark = Column(String, nullable=True)
    gender = Column(String)
    country = Column(String)
    description = Column(String)

