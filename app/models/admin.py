from app.core.db import Base
from sqlalchemy import Boolean, Column, Integer


class Admin(Base):
    is_superuser = Column(Boolean)
    user_id = Column(Integer)
