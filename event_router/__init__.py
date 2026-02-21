"""
The Autonomous Cross-Platform Event Router (ACR) is a robust system designed to efficiently route events across multiple platforms. It ensures optimal delivery with minimal latency by adapting to platform-specific protocols and constraints.

Components:
- EventListener: Captures events from various sources.
- PlatformAdapter: Handles platform-specific routing logic.
- RouterBrain: Makes intelligent routing decisions based on event type, priority, and platform availability.
- MonitoringSystem: Tracks system health and performance metrics.

Key Features:
- Real-time event capturing
- Adaptive routing strategies
- Fault tolerance and self-healing
- Performance monitoring and analytics
"""

from .event_listener import EventListener
from .platform_adapter import PlatformAdapter
from .router_brain import RouterBrain
from .monitoring_system import MonitoringSystem

__version__ = "1.0.0"