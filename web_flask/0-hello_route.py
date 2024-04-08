#!/usr/bin/python3
"""Module to start a Flask web application

    Returns:
        string: a web page
    """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Function to start a Flask web app with a return of 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
