#!/usr/bin/python3
"""Contains new engine DBStorage"""
from os import getenv
from sqlalchemy import create_engine
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.user import User
from models.review import Review
from sqlalchemy.orm import scoped_session, sessionmaker
# import models


class DBStorage:
    """Definition of the DBStorage class"""
    class_models = {
        "City": City,
        "State": State,
        "User": User,
    }
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of db storage class"""
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
        HBNB_ENV = getenv("HBNB_ENV")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the  current database session"""
        '''
        data = {}
        for clas in class_models:
            if cls is None or cls is class_models[clas] or cls is clas:
                class_objs = self.__session.query(class_models[clas]).all()
                for obj in class_objs:
                    key = obj.__class__.__name__+ '.'+ obj.id
                    data[key] = obj
        return(data)
        '''
        '''
        if cls:
            class_objs = self.__session.query(cls).all()
        else:
            class_objs = self.__session.query(State).all()
        return {obj.id: obj for obj in class_objs}
        '''
        data = {}
        if cls:
            if isinstance(cls, str):
                cls = self.class_models.get(cls)
                if cls is None:
                    raise ValueError(f"Class {cls} is not a valid model")

            if cls not in self.class_models.values():
                raise ValueError(f"Class {cls} is not valid Model")

            if cls not in self.class_models.values():
                raise ValueError(f"'{cls}' is not recognized")

            class_objs = self.__session.query(cls).all()
            for obj in class_objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                data[key] = obj

        else:
            for clas in self.class_models.values():
                class_objs = self.__session.query(clas).all()
                for obj in class_objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    data[key] = obj

        return data

    def new(self, obj):
        """add the object to the current database session"""
        if obj:
            print(f"Adding object to session: {obj}")
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        try:
            print("Committing changes to the database...")
            self.__session.commit()
            print("Changes committed successfully.")
        except Exception as e:
            print(f"Error during commit: {e}")

    def delete(self, obj=None):
        """ delete obj from the current session if not none"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        print("Session intialized:", self.__session)

    def close(self):
        """explicitly dispose of the scoped session"""
        self.__session.remove()
