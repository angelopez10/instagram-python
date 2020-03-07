import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    photo = Column(String(250))
    caption = Column(String(250))
    mentions = Column(String(250), nullable=False)
    adress = Column(String(250))
    user_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)

class Profile(Base):
    __tablename__ = 'profile'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    photo = Column(String(250))
    followers = Column(String(250))
    following = Column(String(250), nullable=False)
    biography = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Timeline(Base):
    __tablename__ = 'timeline'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    posts = Column(String(250))
    followers = Column(String(250))
    ads = Column(String(250), nullable=False)
    likes = Column(String(250))
    comments = Column(String(250))
    profile_id = Column(Integer, ForeignKey('profile.id'))
    profile = relationship(Profile)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')