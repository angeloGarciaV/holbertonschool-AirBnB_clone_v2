#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        """ db ==>  means let's go for SQLAlchemy logic"""
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        name = ""

    @property
    def cities(self):
        """City getter"""
        l_cities = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                l_cities.append(city)
        return l_cities
