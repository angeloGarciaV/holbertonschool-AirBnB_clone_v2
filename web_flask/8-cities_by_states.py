#!/usr/bin/python3
"""
flask model
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False
storage.all()


@app.route('/cities_by_states')
def cities_by_states():
    """ return all cities by states"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_data(exception):
    """reload data"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
