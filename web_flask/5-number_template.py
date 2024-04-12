#!/usr/bin/python3
"""Module to start a Flask web application

    Returns:
        string: a web page
    """
from flask import Flask, render_template, abort

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """Function to start a Flask web app with a return of 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Function to start a Flask web app with a return of '/hbnb'"""
    return "/hbnb"


@app.route("/c/<text>")
def dispC(text):
    """Function with a return of '/c/<text>'"""
    newText = text.replace('_', " ")
    return f'C {newText}'


@app.route("/python", defaults={'text': 'is_cool'})
@app.route("/python/<text>")
def dispPython(text):
    """Function with a return of '/python/<text>'"""
    newText = text.replace('_', " ")
    return f'Python {newText}'


@app.route("/number/<n>")
def ifInt(n):
    """display “n is a number” only if n is an integer"""
    try:
        number = int(n)
    except Exception as e:
        abort(404)
    return f'{number} is a number'


@app.route("/number_template/<n>")
def number_template(n):
    """display “n is a number” only if n is an integer"""
    try:
        number = int(n)
    except Exception as e:
        abort(404)
    return render_template("5-number.html", n=number)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
