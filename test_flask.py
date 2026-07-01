#!/usr/bin/env python
"""Minimal Flask test app"""
from flask import Flask, jsonify

print("Creating Flask app...")
app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"status": "Flask is running!"})

@app.route('/health')
def health():
    return jsonify({"status": "OK"})

if __name__ == '__main__':
    print("Starting Flask on 0.0.0.0:5000...")
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
