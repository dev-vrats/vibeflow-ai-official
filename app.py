import streamlit as st
import asyncio
import io

# We will import our modules directly for Streamlit caching, acting as an integrated approach
# In a true decoupled microservices architecture, we would use requests library to call FastAPI (api.py)
from modules.core_ai import VisionAssistant
from modules.maps_logic import MapsRouter
from modules.firebase_sync import QueueManager
from ui.components import render_header, render_alert, render_route_card

# Initialize components
st.set_page_config(page_title="VibeFlow AI", page_icon="🎫", layout="centered")

@st.cache_resource
def get_ai_assistant():
    return VisionAssistant()

@st.cache_resource
def get_maps_router():
    return MapsRouter()

@st.cache_resource
def get_queue_manager():
    return QueueManager()

def main():
    render_header()
    
    tab1, tab2, tab3 = st.tabs(["Vision & Routing", "Queue Alerts", "Accessibility"])
    
    with tab1:
        st.subheader("Predictive Crowd Routing & Vision Assistant")
        st.markdown("Upload a photo of your ticket or a stadium sign to get context-aware directions.")
        
        uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
        if uploaded_file:
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
            
            if st.button("Interpret & Route"):
                with st.spinner("Analyzing with Gemini 1.5 Pro..."):
                    ai = get_ai_assistant()
                    image_bytes = uploaded_file.getvalue()
                    analysis_result = ai.interpret_image(image_bytes, "Extract ticket details.")
                    st.success(f"**Analysis Result:** {analysis_result}")
                    
                    if "Gate 4" in analysis_result or "Seat" in analysis_result:
                        st.info("Generating optimal route based on crowd density...")
                        router = get_maps_router()
                        route = router.get_optimal_route("Main Entrance", "Gate 4")
                        render_route_card(route)

    with tab2:
        st.subheader("Real-time 'Fresh-Drop' Queueing")
        st.markdown("Simulate a geofenced notification when your concession order is ready.")
        
        if st.button("Simulate Approach to Concession Stand"):
            with st.spinner("Syncing with Firestore..."):
                qm = get_queue_manager()
                result = asyncio.run(qm.fresh_drop_alert_queue("user_123", "Spicy Bites Combo"))
                
                if result["status"] == "triggered":
                    notif = result["notification"]
                    render_alert(notif["title"], notif["message"], "success")

    with tab3:
        st.subheader("Describe Surroundings (Accessibility First)")
        st.markdown("Upload a photo of your surroundings for an audio description.")
        
        acc_file = st.file_uploader("Upload Surroundings Photo", type=["jpg", "png", "jpeg"], key="acc_file")
        if acc_file:
            if st.button("Describe Surroundings"):
                with st.spinner("Analyzing environment..."):
                    ai = get_ai_assistant()
                    description = ai.describe_surroundings(acc_file.getvalue())
                    st.success("Description Ready")
                    st.write(description)
                    # Simulated text-to-speech output
                    st.audio(io.BytesIO(b"fake_audio_bytes"), format="audio/mp3")
                    st.caption("🔊 (Simulated Audio Playback)")

if __name__ == "__main__":
    main()
