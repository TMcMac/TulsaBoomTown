#!/usr/bin/python3
""" the main Flask application for our API """
from api.v1.views import app_views
from os import environ
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.teardown_appcontext
def close_db(error):
    """ closes the connection to MySQL """
    pass


@app.errorhandler(404)
def not_found(error):
    """ 404 handler """
    return {"error": "Not found"}, 404


if __name__ == "__main__":
    host = environ.get("API_HOST")
    port = environ.get("API_PORT")
    if not host:
        host = "0.0.0.0"
    if not port:
        port = "5000"
    app.run(host=host, port=port, threaded=True)
