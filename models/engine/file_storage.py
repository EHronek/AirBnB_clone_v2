#!/usr/bin/python3
""" Defines a class storage that serializes instances to a json file
    and desirializes JSON file to instances"""
import json
import models


class FileStorage:
    """serializes instances to json file and desirializes json file
    to instances"""
    __file_path = 'file.json'
    __objects = {}

    def delete(self, obj=None):
        """Deletes obj from __objects if its inside else it Returns"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]

    def all(self, cls=None):
        """Intially returned the dictionary __objects
           returns the list of all objects of one type of class
        """
        if cls:
            return {k: v for k, v in self.__objects.items()
                    if isinstance(v, cls)}

        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to json file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """ Deserializes the json file to __objects (only if the JSON
        file(__file_path) exists: otherwise, do nothing. If the file
        doesn't exist, no exemption should be raised"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review
        from models.city import City

        try:
            with open(self.__file_path, 'r') as f:
                for data in json.load(f).values():
                    class_name = data["__class__"]
                    del data["__class__"]
                    self.new(eval(class_name)(**data))
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

    def close(self):
        """call reload method for deserializing the JSON file objects"""
        self.reload()
