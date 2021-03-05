#!/usr/bin/python3
"""Starts a flask session"""
from os import environ
import uuid
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/test_index', strict_slashes=False)
def boom():
    """Hosts the index page so we can look at it"""
    return render_template('index.html',
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
