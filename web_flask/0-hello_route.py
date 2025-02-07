#!/usr/bin/env python3
"""
Starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays hello HBNB! when root url is hit"""
    return "Hello HBNB!"

if __name__ == "__main__":
    # Listen in all available network address in my local machine
    app.run(host='0.0.0.0', port=5000)
