#!/usr/bin/python3
"""
starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
    /number_template/<n>: Displays an HTML page only if <n> is an integer.
        - Displays the value of <n> in the body.
    /number_odd_or_even/<n>: Displays an HTML page only if <n> is an integer.
        - States whether <n> is even or odd in the body.
"""

from flask import Flask, render_template

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


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    """
    function to display even or odd number
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
