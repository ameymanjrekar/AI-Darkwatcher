import streamlit as st
import json
import os
import urllib.parse
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(
    page_title="AI DarkWatch™ - Global AI Threat Observatory",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Dark Aesthetic Styling (No framework branding)
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at 50% 0%, #1e112a 0%, #020617 70%);
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    header, footer {visibility: hidden;}
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2.5rem;
        max-width: 1000px;
    }
    .metric-card {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 14px 18px;
        backdrop-filter: blur(12px);
    }
    .badge-critical {
        background: rgba(239, 68, 68, 0.15);
        color: #f87171;
        border: 1px solid rgba(239, 68, 68, 0.3);
        padding: 2px 8px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 700;
        font-family: monospace;
    }
    .badge-solution {
        background: rgba(16, 185, 129, 0.15);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.3);
        padding: 2px 8px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 700;
        font-family: monospace;
    }
    .wa-btn {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #10b981;
        color: white !important;
        padding: 6px 12px;
        border-radius: 8px;
        text-decoration: none;
        font-size: 12px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "incidents.json")
HTML_PATH = os.path.join(BASE_DIR, "index.html")

# Load data
data = {}
if os.path.exists(DATA_PATH):
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        st.error(f"Error loading incidents.json: {e}")

# Header (Branding free of framework mentions)
st.markdown("""
<div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 12px; margin-bottom: 16px;">
    <div style="display: flex; align-items: center; gap: 12px;">
        <div style="background: linear-gradient(135deg, #ef4444, #be123c); width: 40px; height: 40px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 22px; box-shadow: 0 0 16px rgba(239, 68, 68, 0.4);">
            ⚡
        </div>
        <div>
            <div style="font-size: 22px; font-weight: 900; background: linear-gradient(90deg, #f87171, #f472b6, #fde047); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                AI DarkWatch™
            </div>
            <div style="font-size: 12px; color: #94a3b8;">
                Curated by Amey Manjrekar • Global Threat Gauge, Incident Feed & Community Ratings
            </div>
        </div>
    </div>
    <div style="display: flex; gap: 8px;">
        <a href="https://www.linkedin.com/in/ameymanjrekar" target="_blank" style="background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); padding: 4px 10px; border-radius: 8px; font-size: 11px; text-decoration: none; font-weight: 600;">
            💼 DM on LinkedIn
        </a>
        <a href="https://paypal.me/ameymanjrekar" target="_blank" style="background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); padding: 4px 10px; border-radius: 8px; font-size: 11px; text-decoration: none; font-weight: 600;">
            ☕ PayPal Support
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# Top 4 Metrics
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 11px; color: #94a3b8; font-family: monospace;">CURRENT THREAT GAUGE</div>
        <div style="font-size: 24px; font-weight: 900; color: #f87171;">72 / 100</div>
        <div style="font-size: 10px; color: #f87171;">CRITICAL RISK LEVEL</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 11px; color: #94a3b8; font-family: monospace;">PUBLIC AI TRUST</div>
        <div style="font-size: 24px; font-weight: 900; color: #fbbf24;">41.8%</div>
        <div style="font-size: 10px; color: #f87171;">🔻 -16.2% this month</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 11px; color: #94a3b8; font-family: monospace;">ROGUE BOT ALERTS</div>
        <div style="font-size: 24px; font-weight: 900; color: #c084fc;">4 Monitored</div>
        <div style="font-size: 10px; color: #34d399;">Active Sandbox Containment</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 11px; color: #94a3b8; font-family: monospace;">TOP CAUSE</div>
        <div style="font-size: 24px; font-weight: 900; color: #38bdf8;">#1 Unvetted</div>
        <div style="font-size: 10px; color: #94a3b8;">1,120 Open Model Incidents</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# Embedded Interactive Gauge, Wave & Incident System
if os.path.exists(HTML_PATH):
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html_code = f.read()
    components.html(html_code, height=720, scrolling=True)
else:
    st.warning("index.html not found.")

st.write("")

# Contact & License Section
st.markdown("""
<div class="metric-card" style="margin-top: 15px; border: 1px solid rgba(59, 130, 246, 0.3);">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: gap;">
        <div>
            <strong style="color: #60a5fa; font-size: 14px;">Want to Collaborate or License This Project?</strong>
            <p style="margin: 4px 0 0 0; font-size: 12px; color: #94a3b8;">
                Curated by Amey Manjrekar. Reach out for enterprise risk monitoring, custom threat feeds, or partnership opportunities.
            </p>
        </div>
        <div style="display: flex; gap: 10px; margin-top: 8px;">
            <a href="https://www.linkedin.com/in/ameymanjrekar" target="_blank" style="background: #2563eb; color: white !important; padding: 7px 14px; border-radius: 8px; font-size: 12px; font-weight: 600; text-decoration: none;">
                DM on LinkedIn
            </a>
            <a href="https://paypal.me/ameymanjrekar" target="_blank" style="background: #059669; color: white !important; padding: 7px 14px; border-radius: 8px; font-size: 12px; font-weight: 600; text-decoration: none;">
                PayPal Support
            </a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
