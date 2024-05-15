from sqlalchemy import Boolean, Column, Integer

from app.core.db import Base


class Admin(Base):
    is_superuser = Column(Boolean)
    user_id = Column(Integer)
