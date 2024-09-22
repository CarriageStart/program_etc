from flask import Flask, render_template

APP = Flask(__name__)

@APP.route("/hello/<name>")
def hello_name(name):
    return render_template('./hello.html', name=name)

@APP.route("/hello2/<name>")
def hello2_name(name):
    return render_template('./hello2.html', name=name)

if __name__=="__main__":
    APP.run(debug=True)



