#!/usr/bin/env python
"""Test importing the app module"""
import sys
import traceback

print("=" * 50, flush=True)
print("Starting import test...", flush=True)

try:
    print("1. Importing Flask modules...", flush=True)
    from flask import Flask
    print("   ✓ Flask imported", flush=True)
    
    print("2. Importing pandas...", flush=True)
    import pandas as pd
    print("   ✓ Pandas imported", flush=True)
    
    print("3. Importing oracledb...", flush=True)
    import oracledb
    print("   ✓ OracleDB imported", flush=True)
    
    print("4. Importing app module...", flush=True)
    from app import app
    print("   ✓ App imported successfully!", flush=True)
    
    print("5. Checking app routes...", flush=True)
    print(f"   Routes defined: {len(app.url_map._rules)}", flush=True)
    
    print("\n✓ All imports successful!", flush=True)
    print("=" * 50, flush=True)
    
except Exception as e:
    print(f"\n✗ ERROR: {e}", flush=True)
    print("\nTraceback:", flush=True)
    traceback.print_exc()
    sys.exit(1)
