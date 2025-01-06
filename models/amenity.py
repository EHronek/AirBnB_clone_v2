#!/usr/bin/python3
""" Defines the Amenity class"""
from models.base_model import BaseModel, Base
import models
import sqlalchemy
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Defination of the Amenity blueprint"""
    if models.type_storage == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """ initialization """
        super().__init__(*args, **kwargs)
