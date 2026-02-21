from typing import List, Dict, Any
import logging
from .platform_adapter.platformAdapterFactory import PlatformAdapterFactory

class RouterBrain:
    """Makes intelligent routing decisions based on event type and platform availability."""
    
    def __init__(self):
        self.adapters = {}  # Maps platform names to their adapters
        self.logger = logging.getLogger(__name__)
        
    async def initialize_adapters(self, config: Dict[str, Any]) -> None:
        """Initializes all platform adapters based on configuration."""
        for platform in config['platforms']:
            adapter = PlatformAdapterFactory.create_adapter(platform)
            self.adapters[platform] = adapter
            self.logger.info(f"Adapter for {platform} initialized")

    async def route_event(self, event: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Routes an event to the appropriate platforms."""
        results = []
        try:
            # Determine target platforms based on event type and priority
            target_platforms = self._determine_targets(event)
            
            for platform in target_platforms:
                if platform not in self.adapters:
                    raise ValueError(f"Adapter for {platform} not found")
                
                adapter = self.adapters[platform]
                response = await adapter.send_event(event)
                results.append(response)
                
                # Check if the platform is healthy
                health = await adapter.check_health()
                if not health:
                    self._mark_platform_unhealthy(platform)

            return results
            
        except Exception as e:
            self.logger.error(f"Routing failed: {str(e)}")
            raise

    def _determine_targets(self, event: Dict[str, Any]) -> List[str]:
        """Determines which platforms should handle the given event."""
        # Simplified logic; can be extended with actual business rules
        return ['platform1', 'platform2']

    def _mark_platform_unhealthy(self, platform: str) -> None:
        """Mark a platform as unhealthy for routing decisions."""
        self.logger.warning(f"Marking {platform} as unhealthy")