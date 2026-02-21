import logging
from typing import Dict, Any
from aiohttp import ClientSession

class HttpEventListener:
    """Captures events via HTTP requests and converts them into a standard format."""
    
    def __init__(self, endpoint: str, session: ClientSession):
        self.endpoint = endpoint
        self.session = session
        self.logger = logging.getLogger(__name__)
        
    async def capture_event(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Captures an event from the HTTP endpoint and returns it in a standard format."""
        try:
            # Simulate capturing from HTTP endpoint
            async with self.session.post(self.endpoint, json=data) as response:
                result = await response.json()
                self.logger.info(f"Event captured via HTTP: {result}")
                return result
        except Exception as e:
            self.logger.error(f"Failed to capture event: {str(e)}")
            raise

    def __repr__(self):
        return f"HttpEventListener({self.endpoint})"