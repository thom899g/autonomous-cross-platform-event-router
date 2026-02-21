from abc import ABC, abstractmethod
from typing import Dict, Any

class PlatformAdapter(ABC):
    """Abstract base class for platform-specific adapters."""

    @abstractmethod
    def send_event(self, event: Dict[str, Any]) -> bool:
        """Sends an event to the platform and returns True if successful."""
        pass
    
    @abstractmethod
    def handle_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """Processes a response from the platform and returns the result."""
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}()"