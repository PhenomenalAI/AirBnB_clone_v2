#!/usr/bin/python3
"""
starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""

from flask import Flask
from flask import render_template

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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def displays_py(text="is cool"):
    """Displays 'Python' followed by value of text"""
    text = text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def displays_int(n):
    """Displays 'n is anumber' if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def displays_html(n):
    """Displays an html if n is an integer"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
