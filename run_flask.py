#!/usr/bin/env python
"""Simple Flask runner with error logging"""
import os
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Set up logging
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('flask_startup.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

try:
    logger.info("="*60)
    logger.info("Flask Startup Log")
    logger.info("="*60)
    logger.info(f"Python: {sys.version}")
    logger.info(f"CWD: {os.getcwd()}")
    
    logger.info("\nImporting Flask...")
    from flask import Flask
    logger.info("✓ Flask imported")
    
    logger.info("Importing app module...")
    from app import app as flask_app
    logger.info("✓ App module imported")
    
    logger.info("\nStarting Flask server...")
    logger.info("Listen on: 0.0.0.0:5000")
    
    # Run Flask
    flask_app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
    
except SystemExit as e:
    logger.error(f"SystemExit: {e}")
    raise
except Exception as e:
    logger.exception(f"Fatal Error: {type(e).__name__}: {e}")
    sys.exit(1)
