"""Health interface module"""


class HealthInterface:
    """Interface for health check responses"""

    @staticmethod
    def format_response(status):
        """Format health check response"""
        return {
            "message": "Health check response",
            "data": status
        }
