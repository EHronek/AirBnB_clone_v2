#!/usr/bin/env python3
""" Defines the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Defination of the Amenity blueprint"""
    name = ''

    def __init__(self, *args, **kwargs):
        """ initialization """
        super().__init__(*args, **kwargs)
