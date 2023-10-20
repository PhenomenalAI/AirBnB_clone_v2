#!/usr/bin/python3
"""
starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""

from flask import Flask

app = Flask(__name__)


# Defines a route for the root URL ("/") and set strict_slashes to False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def displays_str():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def val_text(text):
    """Displays 'C' followed by value of <text>"""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
