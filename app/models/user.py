from sqlalchemy import Column, Integer, String, Sequence, Boolean

from ..core.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String, nullable=False, unique=True)
    telegram_id = Column(String)
    is_admin = Column(Boolean, default=False)
