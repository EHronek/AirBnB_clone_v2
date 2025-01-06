#!/usr/bin/python3
""" Defines a class State that inherits from BaseModel"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """ Defination of State"""
    if models.type_storage == "db":
        __tablename__ = "states"

        id = Column(String(60), primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")

    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initialization of State """
        super().__init__(*args, **kwargs)

    if models.type_storage != "db":
        @property
        def cities(self):
            """getter for list of city instances related to tge state"""
            list_of_cities = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    list_of_cities.append(city)
            return list_of_cities
