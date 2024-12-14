from sqlalchemy import Column, Integer, String
from .database import Base


class Mission(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String)
    descritption = Column(String)
