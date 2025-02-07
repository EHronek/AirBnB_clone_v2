#!/usr/bin/python3
"""Script starts a Flask web application"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Handles request for root"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Handles request for /hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """Displays 'c' followed by value of text """
    return 'C ' + text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
