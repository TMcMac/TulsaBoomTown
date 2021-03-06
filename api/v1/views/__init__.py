#!/usr/bin/python3
""" creates Blueprint for our API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.companies import *
from api.v1.views.jobs import *
