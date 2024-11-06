# save this as app.py
from flask import Flask
from random import randint


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"+str(randint(0,100))

 