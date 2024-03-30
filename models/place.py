#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

from models.amenity import Amenity, place_amenity
from models.review import Review


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata_obj,
                          Column('place_id', String(60), ForeignKey(
                              'places.id'), primary_key=True, nullable=False),
                          Column('amenity_id', String(60), ForeignKey(
                              'amenities_id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        amenity_ids = []
        reviews = relationship(
            'Review',
            cascade="all, delete, delete-orphan",
            backref='place'
        )
        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False
        )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            """Returns the amenities of the current Place"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, value):
            """Adds amenities to the current Place"""
            if type(value) is Amenity:
                if value.id not in self.amenity_ids:
                    self.amenity_ids.append(value.id)
            else:
                pass

        @property
        def reviews(self):
            """Returns the reviews of this Place"""
            from models import storage
            reviews_of_place = []
            for key, value in storage.all().items():
                cls = key.split('.')[0]
                if cls == 'Review' and value.place_id == self.id:
                    reviews_of_place.append(value)
            return reviews_of_place
