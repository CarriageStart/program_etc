from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)
data = pd.DataFrame(columns=["IP", "Data"])

@app.route('/update', methods=['POST'])
def update_data():
    global data
    new_data = request.json
    ip = request.remote_addr
    new_data['IP'] = ip
    data = data.append(new_data, ignore_index=True)
    return jsonify(data.to_dict(orient='records'))

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)

