# wsgi.py
# pylint: disable=missing-docstring

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello world!"


from flask import Flask, render_template
from longest_word.game import Game

app = Flask(__name__)

@app.route('/')
def home():
    game = Game()
    return render_template('home.html', grid=game.grid)
