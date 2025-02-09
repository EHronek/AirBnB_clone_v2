#!/usr/bin/python3
""" Defines the City class """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class City(BaseModel, Base):
    """ Defination of the City """
    if models.type_storage == "db":
        __tablename__ = "cities"
        id = Column(String(60), primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities")

    else:
        name = ''
        state_id = ''

    def __init__(self, *args, **kwargs):
        """ initialization of the city """
        super().__init__(*args, **kwargs)
