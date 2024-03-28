#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    __tablename__ = 'basemodel'
    id = Column(String(60), uuid.uuid4(), primary_key=True, nullable=False)
    created_at = Column(String, datetime.now(datetime.UTC), nullable=False)
    updated_at_at = Column(String, datetime.now(datetime.UTC))

    def __init__(self, id, created_at, updated_at, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = id
            self.created_at = created_at
            self.updated_at = updated_at
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        if _sa_instance_state:
            del _sa_instance_state
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        from models import storage
        del self
        storage.save()
