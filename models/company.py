#!/usr/bin/python3
""" holds class Company """
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer


class Company(BaseModel, Base):
    """ representation of a Company """
    __tablename__ = "companies"
    name = Column(String(130), nullable=False)
    website = Column(String(230), nullable=False)
    employee_count = Column(Integer, nullable=True)
    industries = Column(String(200), nullable=False)
    tech_stack = Column(String(200), nullable=True)
    jobs_board = Column(String(230), nullable=True)
    logo_file = Column(String(60), nullable=False)

    def __init__(self, *args, **kwargs):
        """ constructor """
        super().__init__(*args, **kwargs)
