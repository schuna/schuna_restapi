from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(80), unique=True)
    email = Column(String(80), unique=True)
    password = Column(String(80))
    posts = relationship("Post", cascade="all, delete", back_populates='user', lazy='joined')
    inbodies = relationship("InBody", cascade="all, delete", back_populates="user", lazy="joined")
