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
    """Function with a return of '/c/<text>'"""
    newText = text.replace('_', " ")
    return f'C {newText}'


@app.route("/python", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def dispPython(text):
    """Function with a return of '/python/<text>'"""
    newText = text.replace('_', " ")
    return f'Python {newText}'


@app.route("/number/<n>", strict_slashes=False)
def ifInt(n):
    """display “n is a number” only if n is an integer"""
    try:
        number = int(n)
    except Exception:
        return f'{n} is not a number'

    return f'{number} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
