from random import choice
from flask import Flask
from os import environ

app = Flask(__name__)
options_file = environ.get("OPTIONS_FILE","options.txt")
def load_options(file_path):
    with open(file_path,"r",encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents.split()

options = load_options(options_file)
# options = ["first", "second", "third"]

@app.route("/")
def pick_word():
    return choice(options)