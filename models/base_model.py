#!/usr/bin/env python3
"""Defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ base class for all the other classes on the project"""
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
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            storage.new(self)

    def save(self):
        """ updates the public intance attribute update_at with the
        with the current date time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of `__dict__`
        of the instance"""
        obj_dict_copy = self.__dict__.copy()
        obj_dict_copy['__class__'] = type(self).__name__
        obj_dict_copy['created_at'] = self.created_at.isoformat()
        obj_dict_copy['updated_at'] = self.updated_at.isoformat()
        return obj_dict_copy

    def __str__(self):
        """ prints a user friendly string representation of the object"""
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
