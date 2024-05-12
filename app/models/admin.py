from app.core.db import Base
from sqlalchemy import Boolean, Column


class Admin(Base):
    is_superuser = Column(Boolean)
