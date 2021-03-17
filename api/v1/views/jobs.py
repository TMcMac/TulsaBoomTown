#!/usr/bin/python3
""" handles basic status check """

from api.v1.views import app_views
from flask import jsonify, request
from models import storage
from models.remote import Remote
from models.local import Local


@app_views.route('/jobs', methods=['GET'], strict_slashes=False)
def jobs():
    """ Returns the company card info from our database """
    raw_remote = storage.all(Remote).values()
    raw_local = storage.all(Local).values()
    temp = []
    out = {}

    for j in raw_remote:
        temp.append(j.to_dict())
    out.update({"remote": temp})

    temp = []

    for j in raw_local:
        temp.append(j.to_dict())
    out.update({"local": temp})

    return jsonify(out)
