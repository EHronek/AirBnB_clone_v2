#!/usr/bin/env python3
""" Defines the class review that inherits from the BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Blueprint for the how to Review"""
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """ Initialization of review"""
        super().__init__(*args, **kwargs)
