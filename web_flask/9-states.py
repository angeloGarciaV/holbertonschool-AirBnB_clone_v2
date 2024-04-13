#!/usr/bin/python3
"""Module to start a Flask web application

    Returns:
        string: a web page
    """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    state_dic = storage.all(State)
    state = None
    for obj in state_dic.values():
        if obj.id == id:
            state = obj
    return render_template('9-states.html', states=state_dic, id=id,
                           state=state)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ Function that removes the current SQL Alchemy Session after each
    request. """
    storage.close()
