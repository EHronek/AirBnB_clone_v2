#!/usr/bin/env python3
""" Defines the City class """
from models.base_model import BaseModel


class City(BaseModel):
    """ Defination of the City """
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """ initialization of the city """
        super().__init__(*args, **kwargs)
