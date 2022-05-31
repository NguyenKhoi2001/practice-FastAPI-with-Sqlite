from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True,index=True)
    tittle = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    creator = relationship('User', back_populates='blogs')

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blogs = relationship('Blog', back_populates='creator')