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


@app.route('/states_list')
def states_list():
    """Display a list of states"""
    states_list = storage.all(State).values()
    return render_template('7-states_list.html', states=states_list)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """After each request, remove the SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
