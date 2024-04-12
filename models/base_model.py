#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object
time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Add classes attributes"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    """A base class for all hbnb models"""

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                kwargs["created_at"] = datetime.now()
            else:
                kwargs['created_at'] = (datetime.strptime(kwargs['created_at'],
                                                          '%Y-%m-%dT%H:%M:%S.'
                                                          '%f'))
            if "updated_at" not in kwargs:
                kwargs["updated_at"] = datetime.now()
            else:
                kwargs['updated_at'] = (datetime.strptime(kwargs['updated_at'],
                                                          '%Y-%m-%dT%H:%M:%S.'
                                                          '%f'))
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        cp_dict = dict(self.__dict__)
        if '_sa_instance_state' in cp_dict:
            del cp_dict['_sa_instance_state']
        return '[{}] ({}) {}'.format(cls, self.id, cp_dict)

    def __repr__(self):
        """
        Official representation of the object
        """
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Delete the current instance from the models.storage"""
        models.storage.delete(self)

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict
