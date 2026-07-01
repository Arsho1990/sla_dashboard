#!/usr/bin/env python
"""Flask wrapper with lazy loading to avoid database connection on import"""
import os
import sys

os.chdir(r'd:\ARSALAN\Sla_dashboard')
sys.path.insert(0, r'd:\ARSALAN\Sla_dashboard')

print("=" * 60, flush=True)
print("Starting SLA Dashboard Server", flush=True)
print("=" * 60, flush=True)

try:
    print("[1/3] Loading Flask framework...", flush=True)
    from flask import Flask
    print("[✓] Flask loaded", flush=True)
    
    print("[2/3] Importing application module...", flush=True)
    # Import with a timeout-like approach by setting sys.settimeout
    import signal
    
    def timeout_handler(signum, frame):
        raise TimeoutError("Module import timed out")
    
    # Set a 10 second timeout for the import
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(10)
    
    try:
        from app import app as flask_app
        signal.alarm(0)  # Cancel the alarm
        print("[✓] Application module loaded", flush=True)
    except TimeoutError:
        signal.alarm(0)
        print("[✗] TIMEOUT: Application module import took too long", flush=True)
        print("    This usually means the database connection is hanging", flush=True)
        sys.exit(1)
    
    print("[3/3] Starting server on 0.0.0.0:5000...", flush=True)
    print("-" * 60, flush=True)
    
    flask_app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        use_reloader=False,
        threaded=True
    )
    
except KeyboardInterrupt:
    print("\n[!] Server stopped by user", flush=True)
    sys.exit(0)
except Exception as e:
    print(f"[✗] FATAL ERROR: {type(e).__name__}: {e}", flush=True)
    import traceback
    traceback.print_exc()
    sys.exit(1)
