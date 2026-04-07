"""Health service module"""


class HealthService:
    """Service for health check operations"""

    @staticmethod
    def get_health_status():
        """Get health status of the application"""
        return {
            "status": "healthy",
            "version": "1.0.0"
        }
