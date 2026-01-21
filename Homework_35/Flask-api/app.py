from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"name": "John", "age": 30} 
    return jsonify(data)