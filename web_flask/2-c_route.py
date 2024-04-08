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


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Function to start a Flask web app with a return of '/hbnb'"""
    return "/hbnb"


@app.route("/c/<text>", strict_slashes=False)
def dispC(text):
    newText = text.replace('_', " ")
    return f'C {newText}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
