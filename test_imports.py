#!/usr/bin/env python
"""Test which import is hanging"""
import sys

print("1. Importing Flask", flush=True)
sys.stdout.flush()
from flask import Flask
print("✓ Flask imported", flush=True)

print("2. Importing pandas", flush=True)
sys.stdout.flush()
import pandas as pd
print("✓ pandas imported", flush=True)

print("3. Importing oracledb", flush=True)
sys.stdout.flush()
import oracledb
print("✓ oracledb imported", flush=True)

print("4. Importing app module", flush=True)
sys.stdout.flush()
from app import app
print("✓ app module imported", flush=True)

print("5. Done!", flush=True)
