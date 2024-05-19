from sqlalchemy import Column, DateTime, Integer, String, Text

from app.core.db import Base


class User(Base):
    user_id = Column(Integer)
    user_name = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    chat_id = Column(Integer)
    subscribe_date = Column(DateTime)
    unsubscribe_date = Column(DateTime, nullable=True)
    avatar = Column(Text, nullable=True)
    utm_mark = Column(String, nullable=True)
    gender = Column(String)
    country = Column(String)
    description = Column(String)
