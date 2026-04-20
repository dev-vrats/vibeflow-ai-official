import streamlit as st

def render_header():
    """Renders the high-contrast accessiblity header."""
    st.markdown(
        """
        <style>
        /* Global App Styling for Glassmorphism & Animations */
        .stMainBlockContainer {
            background: transparent !important;
        }
        .stApp {
            background: linear-gradient(-45deg, #0f172a, #1e1b4b, #0f172a, #172554) !important;
            background-size: 400% 400% !important;
            animation: gradientBG 15s ease infinite !important;
        }
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Streamlit Button Styling */
        .stButton > button {
            background: rgba(255, 255, 255, 0.05) !important;
            backdrop-filter: blur(10px) !important;
            -webkit-backdrop-filter: blur(10px) !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            color: #ffffff !important;
            border-radius: 8px !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
        }
        .stButton > button:hover {
            background: rgba(255, 255, 255, 0.15) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2) !important;
            border-color: rgba(255, 255, 255, 0.4) !important;
            color: #ffffff !important;
        }

        /* File Uploader styling */
        .stFileUploader {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 12px;
            padding: 10px;
            border: 1px dashed rgba(255, 255, 255, 0.3);
            transition: all 0.3s ease;
        }
        .stFileUploader:hover {
            border-color: rgba(255, 255, 255, 0.6);
            background: rgba(255, 255, 255, 0.06);
        }

        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 8px;
            padding: 5px;
            backdrop-filter: blur(5px);
        }
        
        .stTabs [data-baseweb="tab"] p {
            color: #e2e8f0;
            transition: color 0.3s ease;
        }
        
        .header {
            background: rgba(26, 26, 29, 0.6);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #F8F9FA;
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 20px;
            text-align: center;
            font-family: 'Inter', sans-serif;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            transition: transform 0.3s ease;
        }
        .header:hover {
            transform: translateY(-3px);
        }
        .header h1 {
            margin: 0;
            font-weight: 700;
            background: -webkit-linear-gradient(45deg, #60a5fa, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .header p {
            margin: 0;
            font-weight: 300;
            color: #e2e8f0;
            margin-top: 5px;
        }
        </style>
        <div class="header">
            <h1>🎫 VibeFlow AI</h1>
            <p>Your Agentic Event Concierge</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_alert(title: str, message: str, type: str = "info"):
    """Renders a custom high-contrast alert, used for Fresh-Drop queueing."""
    colors = {
        "success": ("rgba(198, 246, 213, 0.2)", "#9ae6b4", "rgba(72, 187, 120, 0.4)"),
        "info": ("rgba(235, 248, 255, 0.2)", "#90cdf4", "rgba(66, 153, 225, 0.4)"),
        "warning": ("rgba(254, 235, 200, 0.2)", "#fbd38d", "rgba(237, 137, 54, 0.4)"),
        "error": ("rgba(254, 215, 215, 0.2)", "#feb2b2", "rgba(245, 101, 101, 0.4)")
    }
    bg_col, text_col, border_col = colors.get(type, colors["info"])
    
    st.markdown(
        f"""
        <div style="background: {bg_col}; backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); color: {text_col}; padding: 1.2rem; border-radius: 12px; margin: 10px 0; border: 1px solid {border_col}; box-shadow: 0 4px 15px rgba(0,0,0,0.1); transition: transform 0.3s ease, box-shadow 0.3s ease;" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 6px 20px rgba(0,0,0,0.2)';" onmouseout="this.style.transform='none'; this.style.boxShadow='0 4px 15px rgba(0,0,0,0.1)';">
            <h4 style="margin: 0; display: flex; align-items: center; gap: 8px;">✨ {title}</h4>
            <p style="margin: 5px 0 0 0; font-weight: 300;">{message}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_route_card(route_data: dict):
    st.markdown(
        f"""
        <div style="background: rgba(45, 55, 72, 0.4); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); color: #F7FAFC; padding: 1.8rem; border-radius: 12px; border-left: 5px solid #48BB78; border-top: 1px solid rgba(255,255,255,0.1); border-right: 1px solid rgba(255,255,255,0.1); border-bottom: 1px solid rgba(255,255,255,0.1); margin: 15px 0; box-shadow: 0 8px 32px rgba(0,0,0,0.2); transition: all 0.3s ease;" onmouseover="this.style.transform='scale(1.02)'; this.style.boxShadow='0 12px 40px rgba(0,0,0,0.3)';" onmouseout="this.style.transform='none'; this.style.boxShadow='0 8px 32px rgba(0,0,0,0.2)';">
            <h3 style="margin-top: 0; color: #68D391; display: flex; align-items: center; gap: 8px;">📍 Optimum Route Found</h3>
            <div style="display: flex; flex-direction: column; gap: 8px; font-weight: 300; margin-top: 10px;">
                <div><strong style="color: #A0AEC0;">Path:</strong> <span style="background: rgba(255,255,255,0.1); padding: 2px 8px; border-radius: 4px;">{route_data.get('best_route_path', 'N/A')}</span></div>
                <div><strong style="color: #A0AEC0;">ETA:</strong> <span style="background: rgba(255,255,255,0.1); padding: 2px 8px; border-radius: 4px;">{route_data.get('eta_mins', 'N/A')} mins</span></div>
                <div><strong style="color: #A0AEC0;">Crowd Density:</strong> <span style="background: rgba(255,255,255,0.1); padding: 2px 8px; border-radius: 4px;">{route_data.get('crowd_density', 'N/A')}</span></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
