#!/usr/bin/python3
""" handles basic status check """

from api.v1.views import app_views
from flask import jsonify, request
from models import storage
from models.company import Company


@app_views.route('/companies', methods=['GET'], strict_slashes=False)
def companies():
    """ Returns the company card info from our database """
    raw = storage.all(Company).values()
    out = []
    for c in raw:
        out.append(c.to_dict())
    return jsonify(out)
