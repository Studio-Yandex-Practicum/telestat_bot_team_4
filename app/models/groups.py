from sqlalchemy import Column, String, Boolean

from app.core.db import Base


class Groups(Base):
    group_id = Column(String)
    group_name = Column(String)
    is_choosed = Column(Boolean, default=False)
