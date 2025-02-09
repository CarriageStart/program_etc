from flask import Flask, request, url_for

app = Flask(__name__)
url = "http://127.0.0.1:5000"

@app.route("/")
def index():
    user_url = url_for("show_user_profile", username="John")
    post_url = url_for("show_post", year=2023, month="04", day="01")
    return f"User URL: <a href={url}{user_url}>'User Profile'</a><br>\
        Post URL: <a href={url}{post_url}>Post</a>"

@app.route("/user/<username>")
def show_user_profile(username):
    return f'{username}의 프로필 페이지'

@app.route("/post/<year>/<month>/<day>")
def show_post(year, month, day):
    return f"Post for {year}/{month}/{day}"

@app.route('/static-example')
def static_example():
    return f'정적 파일 URL: {url_for("static",filename="style.css")}'

@app.route('/absolute')
def absolute():
    return f'외부 절대 URL: {url_for("index", _external=True)}'

@app.route('/https')
def https():
    return f'HTTPS 절대 URL: {url_for("index", _scheme="https",_external=True)}'

# Type Hint
@app.route('/int/<int:var>')
def int_type(var: int) -> str:
    return f"Integer: {var}"

@app.route('/float/<float:var>')
def float_type(var: float) -> str:
    return f"Float: {var}"

@app.route('/path/<path:var>')
def path_type(var: str) -> str:
    return f"Path: {var}"

@app.route('/uuid/<uuid:var>')
def uuid_type(var) -> str:
    print(type(var))
    return f"UUID: {var}"



if __name__=="__main__":
    app.run(debug=True)

