#!/usr/bin/env python3
""" Defines a user that inherit from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User blueprint """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
