#!/usr/bin/python3
""" Starts a flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Handles request that hit the root"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Handles request for /hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """Handles request from urls like /c/<text>"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text="is cool"):
    """displays "Python" followed value in text variable"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """displays "n is a number" only if n is an interger """
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an html only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def is_even_or_od(n):
    """Displays a html page only if n is an integer"""
    if n % 2 == 0:
        number_is = 'even'
    else:
        number_is = 'odd'
    return render_template("6-number_odd_or_even.html",
                           n=n, number_is=number_is)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
