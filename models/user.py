#!/usr/bin/env python3
""" Defines a user that inherit from BaseModel"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """ User blueprint """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
