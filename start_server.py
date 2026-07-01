#!/usr/bin/env python
"""Minimal Flask runner"""
import sys
import os
os.chdir(r'd:\ARSALAN\Sla_dashboard')

print("Starting Flask application...", flush=True)

try:
    print("1. Importing Flask...", flush=True)
    from flask import Flask
    print("2. Importing app module...", flush=True)
    from app import app
    print("3. Starting server on port 5000...", flush=True)
    
    # Run Flask without debug mode to avoid reloader issues
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        use_reloader=False,
        use_debugger=False,
        threaded=True
    )
except KeyboardInterrupt:
    print("\nShutdown requested", flush=True)
    sys.exit(0)
except Exception as e:
    print(f"ERROR: {e}", flush=True)
    import traceback
    traceback.print_exc()
    sys.exit(1)
