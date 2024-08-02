#!/usr/bin/env python3
"""Module: Basic flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config for the Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Gets locale from request.
    """
    request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Home Route.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
