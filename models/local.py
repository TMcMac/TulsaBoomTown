#!/usr/bin/python3
""" holds class Company """
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String


class Local(BaseModel, Base):
    """ representation of a Company """
    __tablename__ = "ok_jobs"
    title = Column(String(100), nullable=True)
    company = Column(String(100), nullable=True)
    location = Column(String(200), nullable=False)
    job_link = Column(String(200), nullable=False)

    def __init__(self, *args, **kwargs):
        """ constructor """
        super().__init__(*args, **kwargs)
