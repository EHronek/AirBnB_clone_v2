#!/usr/bin/env python3
""" Defines the City class """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class City(BaseModel, Base):
    """ Defination of the City """
    __tablename__ = "cities"
    id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """ initialization of the city """
        super().__init__(*args, **kwargs)
