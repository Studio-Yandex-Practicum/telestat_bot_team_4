from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text

from core.db import Base


class User(Base):
    __tablename__ = 'user'
    
    tg_user_id = Column(Integer, primary_key=True, unique=True)
    user_name = Column(String)
    chat_id = Column(Integer)
    subscribe_date = Column(DateTime)
    unsubscribe_date = Column(DateTime, nullable=True)
    avatar = Column(Text, nullable=True)
    utm_mark = Column(String, nullable=True)
    gender = Column(String)
    country = Column(String)
    description = Column(String)

