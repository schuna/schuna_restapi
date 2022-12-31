from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String(80))
    image_url_type = Column(String(80))
    caption = Column(String(80))
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates='posts', lazy='joined')
    comments = relationship("Comment", back_populates="post", lazy='joined')
