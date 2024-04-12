#!/usr/bin/python
""" holds class Amenity"""
from models.base_model import BaseModel, Base
from models.place import place_amenity
from os import getenv
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    place_amenities = relationship(
        "Place", secondary=place_amenity, back_populates='amenities')
