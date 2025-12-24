from flask import Flask, jsonify
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route('/health')
def health():
    """Health check endpoint for Kubernetes probes"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'environment': os.getenv('FLASK_ENV', 'development'),
        'version': '1.0.0'
    })


@app.route('/')
def home():
    """Main application endpoint"""
    logger.info("Home endpoint accessed")
    return jsonify({
        'message': 'Welcome to Cloud DevOps Assessment API',
        'environment': os.getenv('FLASK_ENV', 'development'),
        'timestamp': datetime.utcnow().isoformat()
    })


@app.route('/api/info')
def info():
    """API information endpoint"""
    return jsonify({
        'application': 'Cloud DevOps Assessment',
        'version': '1.0.0',
        'framework': 'Flask',
        'environment': os.getenv('FLASK_ENV', 'development'),
        'kubernetes': True,
        'description': 'CI/CD pipeline demonstration for AWS EKS'
    })


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    logger.info(f"Starting Flask application on port {port}")
    logger.info(f"Environment: {os.getenv('FLASK_ENV', 'development')}")
    app.run(host='0.0.0.0', port=port, debug=False)
