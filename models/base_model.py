#!/usr/bin/python3
"""Defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


if models.type_storage == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """ base class for all the other classes on the project"""

    if models.type_storage == "db":
        id = Column(String(60), nullable=False, primary_key=True,
                    default=lambda: str(uuid.uuid4()))
        created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
        updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """ Instantiation of BaseModel class"""

        if kwargs:
            for key, value in kwargs.items():
                fmt = '%Y-%m-%dT%H:%M:%S.%f'
                if key == "__class__":
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, fmt)
                setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = kwargs.get('created_at', datetime.now())
            self.updated_at = kwargs.get('updated_at', datetime.now())
            # models.storage.new(self)
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            models.storage.new(self)
        else:
            #initialize default attributes
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        '''

    def save(self):
        """ updates the public intance attribute update_at with the
        with the current date time"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of `__dict__`
        of the instance"""
        obj_dict_copy = self.__dict__.copy()
        obj_dict_copy['__class__'] = type(self).__name__
        obj_dict_copy['created_at'] = self.created_at.isoformat()
        obj_dict_copy['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in obj_dict_copy:
            del obj_dict_copy["_sa_instance_state"]
        return obj_dict_copy

    def delete(self):
        """Deletes the current instance from the storage"""
        models.storage.delete(self)

    def __str__(self):
        """ prints a user friendly string representation of the object"""
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
