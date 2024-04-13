#!/usr/bin/python3
"""Simple module that starts a Flask web application"""
from models.city import City
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False
#!/usr/bin/python3
""" This script that starts a Flask web application """


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """ Route that display a HTML page with a list of cities
    objects sorted by name """
    city_li = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=city_li)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ Function that removes the current SQL Alchemy Session after each
    request. """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
