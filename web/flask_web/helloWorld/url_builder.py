from flask import Flask, url_for

APP = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the main page~!"

@app.route("/user/<username>")
def profile(username):
    return f'This is the profile of {username}.
        return to Home : {url_for("index")}'


