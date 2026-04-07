"""Health controller module"""
from flask import Blueprint, jsonify
from services.health_service import HealthService
from interfaces.health_interface import HealthInterface

health_bp = Blueprint('health', __name__, url_prefix='/api')


@health_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    status = HealthService.get_health_status()
    response = HealthInterface.format_response(status)
    return jsonify(response), 200
