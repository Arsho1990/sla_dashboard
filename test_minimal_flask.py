#!/usr/bin/env python
"""Minimal Flask app for testing"""
import sys
import os

# Force unbuffered output
os.environ['PYTHONUNBUFFERED'] = '1'

print("TEST: Starting minimal Flask app", flush=True)

try:
    from flask import Flask
    print("TEST: Flask imported", flush=True)
    
    app = Flask(__name__)
    print("TEST: Flask app created", flush=True)
    
    @app.route('/')
    def hello():
        return "Hello World"
    
    print("TEST: Route registered", flush=True)
    print("TEST: Starting server on port 5001...", flush=True)
    
    app.run(host='0.0.0.0', port=5001, debug=False)
    
except Exception as e:
    print(f"TEST ERROR: {e}", flush=True)
    import traceback
    traceback.print_exc(file=sys.stdout)
    sys.exit(1)
