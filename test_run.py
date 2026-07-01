#!/usr/bin/env python
import sys
import traceback

print("Python version:", sys.version)
print("Working directory:", sys.path[0])

try:
    print("\n1. Importing Flask...")
    from flask import Flask
    print("   ✓ Flask imported OK")
    
    print("\n2. Importing app...")
    from app import app
    print("   ✓ App imported OK")
    
    print("\n3. Starting Flask server...")
    print("   Running on http://0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
    
except Exception as e:
    print(f"\n✗ ERROR: {type(e).__name__}: {e}")
    traceback.print_exc()
    sys.exit(1)
