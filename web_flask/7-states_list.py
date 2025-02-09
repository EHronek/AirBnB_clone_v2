#!/usr/bin/python3
"""
Starts a flaks web application
"""
from models import *
from models import storage
from flask import Flask, render_template
from models.state import  State

app = Flask(__name__)



@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays html page with all states listed in alphabetical order"""
    states = storage.all(State).values()
    sorted_states = sorted(list(states), key=lambda s: s.name)
    return render_template("7-states_list.html", states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the current sqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
