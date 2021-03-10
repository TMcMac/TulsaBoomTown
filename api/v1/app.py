#!/usr/bin/python3
""" the main Flask application for our API """
from api.v1.views import app_views
from flask import Flask, jsonify

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_db(error):
    """ closes the connection to MySQL """
    pass


@app.errorhandler(404)
def not_found(error):
    """ 404 handler """
    return {"error": "Not found"}, 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080", threaded=True)
