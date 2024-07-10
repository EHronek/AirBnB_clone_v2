#!/usr/bin/env python3
""" Defines a class State that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """ Defination of State"""
    name = ''
    state_id = ''

    def __init__(self, args, **kwargs):
        """initialization of State """
        super().__init__(*args, **kwargs)
