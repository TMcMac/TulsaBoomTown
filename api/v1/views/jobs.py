#!/usr/bin/python3
""" handles basic status check """

from api.v1.views import app_views
from flask import jsonify, request
from models import storage
from models.job import Job


@app_views.route('/jobs', methods=['GET'], strict_slashes=False)
def jobs():
    """ Returns the company card info from our database """
    raw = storage.all(Job).values()
    out = []
    for j in raw:
        out.append(j.to_dict())
    return jsonify(out)
