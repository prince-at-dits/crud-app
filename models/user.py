from sqlalchemy import Column, Integer, String
from config.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    age = Column(Integer, nullable=True)
