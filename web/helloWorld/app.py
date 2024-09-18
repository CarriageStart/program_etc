from flask import Flask, request, url_for

app = Flask(__name__)

# Index Page
@app.route('/')
def index():
    return 'Hello, World'

# Use variables on parameters
@app.route('/user/<username>')
def hello_user(username):
    return f"Hello, {username}~!"

# Specifying HTTP Method
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Logging in..."
    else:
        return "Log-in Form"

@app.route("/user2/<username>")
def profile(username):
    return f'This is the profile of {username}.\
        return to Home : {url_for("index")}'

if __name__=="__main__":
    app.run(debug=True)


