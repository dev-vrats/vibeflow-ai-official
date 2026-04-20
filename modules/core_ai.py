import os
import io
import base64
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# We simulate the google-genai SDK for the Hack2Skill demo
# In production, we would use: from google import genai
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

load_dotenv()

class VisionAssistant:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY", "mock")

    def interpret_image(self, image_bytes: bytes, prompt: str) -> str:
        """
        Uses Gemini 1.5 Pro to interpret an image of a ticket or stadium sign.
        Returns a mock response for demonstration.
        """
        # Simulated Gemini Vision call
        if b"ticket" in image_bytes or b"TICKET" in image_bytes or b"PNG" in image_bytes or b"JPEG" in image_bytes:
             # Assume it's an Ekana Stadium ticket for demo context
             return "Detected: Ekana Stadium Ticket. Match: Super Kings vs Titans. Gate 4, Block C, Seat 42."
        elif b"sign" in image_bytes:
             return "Detected: Concession Stand Sign. 'Spicy Bites'. Wait time is approximately 5 minutes."
        else:
             return "I analyzed the image. It looks like a standard image. Please provide a ticket or sign for specifics."

    def describe_surroundings(self, image_bytes: bytes) -> str:
        """
        Accessibility feature: Describes surroundings for visually impaired users.
        """
        return "You are currently near Gate 4. To your left is an exit. Straight ahead 50 meters is a restroom. The path is clear of obstacles."

async def analyze_ticket_async(image_bytes: bytes) -> Dict[str, Any]:
    """Async wrapper used by FastAPI"""
    assistant = VisionAssistant()
    # Mocks a network request latency
    import asyncio
    await asyncio.sleep(0.5) 
    response = assistant.interpret_image(image_bytes, "Extract ticket details.")
    return {"status": "success", "analysis": response}

async def describe_surroundings_async(image_bytes: bytes) -> Dict[str, Any]:
    """Async wrapper for accessibility feature"""
    assistant = VisionAssistant()
    import asyncio
    await asyncio.sleep(0.5)
    response = assistant.describe_surroundings(image_bytes)
    return {"status": "success", "description": response}
