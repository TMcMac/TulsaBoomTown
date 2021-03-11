#!/usr/bin/python3
""" holds class Company """
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String


class Job(BaseModel, Base):
    """ representation of a Company """
    __tablename__ = "remote_jobs"
    title = Column(String(100), nullable=True)
    company_name = Column(String(100), nullable=True)
    job_type = Column(String(100), nullable=True)
    category = Column(String(100), nullable=True)
    url = Column(String(230), nullable=True)
    publication_date = Column(String(100), nullable=True)
    candidate_required_location = Column(String(200), nullable=True)

    def __init__(self, *args, **kwargs):
        """ constructor """
        super().__init__(*args, **kwargs)
