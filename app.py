from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

@app.route('/students')
def students():
    return jsonify([])

@app.route('/students/<int:sid>')
def student_by_id(sid):
    return jsonify({"id": sid})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
