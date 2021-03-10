#!/usr/bin/python3
""" contains the BaseModel to interpret our database """

import models
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """ a base class to derive from """
    id = Column(String(60), primary_key=True)

    def __init(self, *args, **kwargs):
        """ constructor """
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        """ returns a dictionary that represents the object """
        out = self.__dict__.copy()
        if "_sa_instance_state" in out:
            del out["_sa_instance_state"]
        return out
