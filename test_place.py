#!/usr/bin/python3
#from models.place import Place
from models.base_model import BaseModel
import uuid

base_obj = BaseModel()
print(base_obj)  # Ensure this prints without error
print(base_obj.id)  # Ensure 'id' is set

class Place(BaseModel):
    """Definition of the class Place"""

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)  # Ensure BaseModel initializes correctly

place = Place(
    city_id="0001",
    user_id="0001",
    name="My_little_house",
    number_rooms=4,
    number_bathrooms=2,
    max_guest=10,
    price_by_night=300,
    latitude=37.773972,
    longitude=-122.431297
)

print(place.to_dict())
#print(place.id)
print(f"Place ID: {place.id}")
print(f"Created At: {place.created_at}")
print(f"Updated At: {place.updated_at}")
