#!/usr/bin/env python3
import sys
print("Python version:", sys.version)
print("Starting Flask server...")

try:
    from flask import Flask
    print("✅ Flask imported")
except Exception as e:
    print(f"❌ Flask import failed: {e}")
    sys.exit(1)

try:
    print("Importing app...")
    import app as flask_app
    print("✅ App imported")
except Exception as e:
    print(f"❌ App import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

try:
    print("Starting app.run()...")
    flask_app.app.run(host='0.0.0.0', port=5000, debug=False)
except Exception as e:
    print(f"❌ Error running app: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
