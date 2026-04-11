"""Flask application entry point"""
import os
from flask import Flask
from flask_cors import CORS
from controllers.health_controller import health_bp

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(health_bp)


@app.route('/')
def index():
    """Index endpoint"""
    return {"message": "Welcome to Plataforma Analítica Territorial"}, 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return {"error": "Not found"}, 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return {"error": "Internal server error"}, 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
