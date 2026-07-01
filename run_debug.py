#!/usr/bin/env python
"""Run Flask with logging enabled"""
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

logger = logging.getLogger(__name__)
logger.info("Starting Flask application...")

try:
    from flask import Flask
    from app import app
    
    logger.info("Flask app loaded successfully")
    logger.info("Starting server on http://0.0.0.0:5000")
    
    # Enable Flask logging
    app.logger.setLevel(logging.DEBUG)
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        use_reloader=False
    )
except Exception as e:
    logger.exception(f"Failed to start: {e}")
    sys.exit(1)
