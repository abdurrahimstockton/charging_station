from flask import Flask
app = Flask(__name__)

@app.route("/")
def shift_left():
    return "<p> Shift Left Testing World!!</p>"

