import logging
from typing import Dict, Any
from time import time

class PerformanceMonitor:
    """Monitors and logs system performance metrics."""

    def __init__(self):
        self.metrics = {}
        self.logger = logging.getLogger(__name__)
        
    def log_metric(self, name: str, value: float) -> None:
        """Logs a performance metric."""
        self.metrics[name] = (time(), value)
        self.logger.info(f"{name}: {value}")

    def get_latency_stats(self) -> Dict[str, Any]:
        """Returns latency statistics."""
        # Simplified example
        return {"min": 0.1, "max": 2.0, "avg": 0.5}

    def alert_on_failure(self, platform: str, error: Exception) -> None:
        """Sends an alert when a failure occurs."""
        self.logger.error(f"Failure in {platform}: {str(error)}")