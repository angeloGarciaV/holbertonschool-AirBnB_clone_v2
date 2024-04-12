#!/usr/bin/python3
""" holds class User"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place",
                          cascade="all, delete, delete-orphan",
                          backref="user")
    reviews = relationship("Review",
                           cascade="all, delete, delete-orphan",
                           backref="user")
