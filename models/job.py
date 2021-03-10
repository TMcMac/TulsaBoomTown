#!/usr/bin/python3
""" holds class Company """
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String


class Job(BaseModel, Base):
    """ representation of a Company """
    __tablename__ = "remote_jobs"
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """ constructor """
        super().__init__(*args, **kwargs)
