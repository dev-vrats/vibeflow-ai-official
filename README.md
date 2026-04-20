# VibeFlow AI 🎫

VibeFlow AI is an agentic Event Concierge designed for large-scale sporting venues (e.g., Ekana Stadium, Lucknow).

## Architecture Elegance
VibeFlow is designed with security, accessibility, and modularity in mind.

1. **Multimodal Agent Orchestration**: 
   - Uses **Vertex AI (Gemini 1.5 Pro)** to intelligently interpret tickets, stadium signs, and user surroundings.
   - Separate handlers ensure that the Vision Assistant scales and is correctly contextualized via internal modules (`core_ai.py`).
2. **Security & Efficiency**:
   - Uses `python-dotenv` to ensure all API Keys (Google Maps, Vertex, Firebase) are strictly kept out of source code.
   - Utilizes `streamlit.cache_data` and `@st.cache_resource` within the Streamlit frontend to store expensive API calls (like Maps routing results and AI object initialization) optimizing performance.
3. **Decoupled Backend**:
   - `api.py` operates as a stand-alone FastAPI instance. Future scale efforts can decouple the frontend completely by routing through containerized endpoints.
4. **Predictive Routing & Async Real-Time Mocking**:
   - `maps_logic.py` integrates Google Maps Platform logic to calculate safe, uncongested paths to a destination.
   - `firebase_sync.py` uses `asyncio` to mock geofenced updates without unnecessarily blocking the main thread.
5. **Accessibility First**:
   - High-contrast custom UI components (`ui/components.py`).
   - Specifically built "Describe Surroundings" capability intended for visually-impaired users with text-to-speech design considerations.

## Running Locally

1. Set up your `.env` from `.env.example`.
2. Install dependencies: `pip install -r requirements.txt`
3. Optional Backend: `uvicorn api:app --reload`
4. Start Frontend: `streamlit run app.py`
5. Test Codebase: `pytest test_suite.py`
