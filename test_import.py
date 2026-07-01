#!/usr/bin/env python
import sys
import traceback

print("Starting import test...")
sys.stdout.flush()

try:
    print("Step 1: Importing Flask...")
    sys.stdout.flush()
    from flask import Flask, request, render_template, send_file, redirect, session, jsonify, url_for
    print("✓ Flask imported")
    
    print("Step 2: Importing pandas...")
    sys.stdout.flush()
    import pandas as pd
    print("✓ pandas imported")
    
    print("Step 3: Importing oracledb...")
    sys.stdout.flush()
    import oracledb
    print("✓ oracledb imported")
    
    print("Step 4: Importing app module...")
    sys.stdout.flush()
    import app
    print("✓ app module imported successfully!")
    
    print("\nStep 5: Testing Flask app...")
    sys.stdout.flush()
    print(f"App name: {app.app.name}")
    print(f"App debug: {app.app.debug}")
    
except Exception as e:
    print(f"\n❌ ERROR: {type(e).__name__}")
    print(f"Message: {str(e)}")
    print("\nFull traceback:")
    traceback.print_exc()
    sys.exit(1)

print("\n✅ All tests passed!")
