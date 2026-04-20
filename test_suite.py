import pytest
import asyncio
from modules.core_ai import VisionAssistant
from modules.maps_logic import MapsRouter
from modules.firebase_sync import QueueManager

def test_vision_assistant_ticket():
    ai = VisionAssistant()
    # Mock ticket implies it has "ticket" in bytes
    result = ai.interpret_image(b"mock ticket image", "test content")
    assert "Ekana Stadium Ticket" in result

def test_vision_assistant_sign():
    ai = VisionAssistant()
    result = ai.interpret_image(b"sign for food", "test content")
    assert "Concession Stand Sign" in result

def test_maps_router():
    router = MapsRouter()
    # Should resolve to the mocked optimum route
    result = router.get_optimal_route("Main Entrance", "Gate 4")
    assert result["status"] == "success"
    assert "best_route_path" in result
    assert result["best_route_path"] == "Via East Corridor"

@pytest.mark.asyncio
async def test_firebase_queue():
    qm = QueueManager()
    result = await qm.fresh_drop_alert_queue("user1", "item_pizza")
    assert result["status"] == "triggered"
    assert "notification" in result
    assert result["notification"]["user_id"] == "user1"
    assert "item_pizza" in result["notification"]["message"]
