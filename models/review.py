#!/usr/bin/python3
""" Defines the class review that inherits from the BaseModel """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Blueprint for the how to Review"""
    if models.type_storage == "db":
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)

    else:
        place_id = ''
        user_id = ''
        text = ''

    def __init__(self, *args, **kwargs):
        """ Initialization of review"""
        super().__init__(*args, **kwargs)
