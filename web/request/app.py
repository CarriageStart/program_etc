from flask import Flask, request, jsonify, make_response

APP = Flask(__name__)

@APP.route('/query')
def query_example():
    language = request.args.get('language')
    return f"Requested Language: {language}"

@APP.route('/json')
def json_example():
    return jsonify({"message": "Hello, World~!"})

@APP.route('/response')
def response_exmple():
    resp = make_response("Hello with header", 400)  # (Body, HTML State Code)
    resp.headers["Custom-Header"] = "Custom-Value"  # Set Header
    return resp

@APP.route('/response2')
def response_exmple2():
    resp = make_response("Hello with header", 200, {'X-Example': 'DirectHeader'})  # (Body, HTML State Code)
    return resp

if __name__=="__main__":
    APP.run(debug=True)

