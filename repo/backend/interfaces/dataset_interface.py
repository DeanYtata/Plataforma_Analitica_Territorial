"""Dataset response formatting helpers."""


class DatasetInterface:
    """Interface for dataset responses"""

    @staticmethod
    def format_dataset_response(message, data):
        """Format a dataset response payload."""
        return {
            "message": message,
            "data": data
        }