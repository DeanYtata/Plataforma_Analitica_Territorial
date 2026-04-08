"""Dataset controller module"""
from flask import Blueprint, jsonify, request
from interfaces.dataset_interface import DatasetInterface
from services.dataset_service import DatasetService

dataset_bp = Blueprint('dataset', __name__, url_prefix='/api')


@dataset_bp.route('/datasets', methods=['GET'])
def list_datasets():
    """List all stored datasets."""
    datasets = DatasetService.list_datasets()
    response = DatasetInterface.format_dataset_response(
        "Datasets retrieved successfully",
        datasets
    )
    return jsonify(response), 200


@dataset_bp.route('/datasets', methods=['POST'])
def create_dataset():
    """Save a dataset in the database."""
    dataset = request.get_json(silent=True) or {}

    if not dataset.get("name"):
        return jsonify({"error": "The field 'name' is required"}), 400

    saved_dataset = DatasetService.save_dataset(dataset)
    response = DatasetInterface.format_dataset_response(
        "Dataset saved successfully",
        saved_dataset
    )
    return jsonify(response), 201