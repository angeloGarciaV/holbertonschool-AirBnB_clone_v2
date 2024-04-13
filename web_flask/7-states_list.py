#!/usr/bin/python3
"""
Simple module that starts a Flask web application
Adds basic template
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """Function to start a Flask web app with a return of 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Function to start a Flask web app with a return of '/hbnb'"""
    return "HBNB"


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


@app.route("/number/<int:n>")
def ifInt(n):
    """display “n is a number” only if n is an integer"""
    return f'{n} is a number'


@app.route("/number_template/<int:n>")
def number_template(n):
    """display “n is a number” only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    """display whether n is odd or even in a template"""
    return render_template("6-number_odd_or_even.html", n=n)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """After each request, remove the SQLAlchemy Session"""
    storage.close()


@app.route('/states_list')
def states_list():
    """Display a list of states"""
    states_list = storage.all(State).values()
    return render_template('7-states_list.html', states=states_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
