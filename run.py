"""
Main application entry point.
Run this file to start the Flask development server.
"""
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)