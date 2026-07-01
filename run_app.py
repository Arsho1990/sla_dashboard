#!/usr/bin/env python
"""
Run Flask app with proper error handling
"""
import sys
import os

# Try to run the app
try:
    from app import app
    print("✓ App imported successfully")
    print("Starting Flask server on http://0.0.0.0:5000...")
    app.run(host='0.0.0.0', port=5000, debug=True)
except Exception as e:
    print(f"✗ Error starting app: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc()
    sys.exit(1)
