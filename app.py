import streamlit as st
import json
import os
import urllib.parse
import streamlit.components.v1 as components

# Streamlit Page Setup
st.set_page_config(
    page_title="AI DarkWatch™ - Global Threat & Autonomous Agent Observatory",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# High-End Dark Glassmorphism Styling
st.markdown("""
<style>
    /* Dark cyber theme */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #1e112a 0%, #020617 70%);
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    header, footer {visibility: hidden;}
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
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

# Header Banner
st.markdown("""
<div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 12px; margin-bottom: 16px;">
    <div style="display: flex; align-items: center; gap: 12px;">
        <div style="background: linear-gradient(135deg, #ef4444, #be123c); width: 38px; height: 38px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 20px; box-shadow: 0 0 16px rgba(239, 68, 68, 0.4);">
            ⚡
        </div>
        <div>
            <div style="font-size: 20px; font-weight: 900; background: linear-gradient(90deg, #f87171, #f472b6, #fde047); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                AI DarkWatch™
            </div>
            <div style="font-size: 12px; color: #94a3b8;">
                Real-Time AI Exploits, Autonomous Agent Actions & Plain-English Defenses
            </div>
        </div>
    </div>
    <div>
        <span style="background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); padding: 4px 10px; border-radius: 20px; font-size: 11px; font-mono; font-weight: 700;">
            ● STREAMLIT CLOUD LIVE
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# Top 4 Metrics
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 11px; color: #94a3b8; font-family: monospace;">PUBLIC AI TRUST</div>
        <div style="font-size: 24px; font-weight: 900; color: #fbbf24;">41.8%</div>
        <div style="font-size: 10px; color: #f87171;">🔻 -16.2% this month</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 11px; color: #94a3b8; font-family: monospace;">VERIFIED HARMS</div>
        <div style="font-size: 24px; font-weight: 900; color: #f87171;">3,200+</div>
        <div style="font-size: 10px; color: #94a3b8;">AIID & CVE Index</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 11px; color: #94a3b8; font-family: monospace;">AGENT ESCAPES</div>
        <div style="font-size: 24px; font-weight: 900; color: #c084fc;">4 Live</div>
        <div style="font-size: 10px; color: #34d399;">All Sandbox-Contained</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 11px; color: #94a3b8; font-family: monospace;">TOP RISK CAUSE</div>
        <div style="font-size: 24px; font-weight: 900; color: #38bdf8;">#1 Unvetted</div>
        <div style="font-size: 10px; color: #94a3b8;">Open-Source Weights</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# Embedded Interactive Wave & Radar
if os.path.exists(HTML_PATH):
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html_code = f.read()
    components.html(html_code, height=640, scrolling=True)
else:
    st.warning("index.html not found.")

st.write("")

# Streamlit Native Explorer Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🤖 Autonomous Agent Actions", 
    "🏢 Model Culprit Rankings", 
    "🛡️ Fixes & Solutions", 
    "💬 1-Click WhatsApp Alerts"
])

with tab1:
    st.subheader("Autonomous AI Bots Doing Harm (In Plain English)")
    for bot in data.get("agent_actions", []):
        with st.container():
            st.markdown(f"""
            <div class="metric-card" style="margin-bottom: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <strong style="color: #c084fc; font-family: monospace;">{bot['agent']}</strong>
                    <span class="badge-critical">{bot['status']}</span>
                </div>
                <p style="margin: 6px 0 0 0; font-size: 13px; color: #cbd5e1;">{bot['detail']}</p>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.subheader("Which AI Models & Companies Cause The Most Issues?")
    for item in data.get("model_rankings", []):
        st.markdown(f"""
        <div class="metric-card" style="margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center;">
            <div>
                <span style="font-weight: 900; color: #f87171; font-family: monospace; margin-right: 8px;">#{item['rank']}</span>
                <strong style="font-size: 14px; color: #f8fafc;">{item['name']}</strong>
                <div style="font-size: 12px; color: #94a3b8; margin-top: 2px;">{item['risk']}</div>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 18px; font-weight: 900; color: #f87171; font-family: monospace;">{item['incidents']}</div>
                <div style="font-size: 10px; color: #64748b;">Incidents</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.subheader("Emerging Fixes & Active Defenses")
    for sol in data.get("solutions", []):
        st.markdown(f"""
        <div class="metric-card" style="margin-bottom: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <strong style="color: #34d399; font-size: 14px;">{sol['title']}</strong>
                <span class="badge-solution">{sol['tag']}</span>
            </div>
            <p style="margin: 6px 0 0 0; font-size: 13px; color: #cbd5e1;">{sol['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.subheader("Send Live Incident Summaries to WhatsApp")
    for inc in data.get("incidents", []):
        msg_text = f"🚨 *AI DarkWatch Alert*\n\n*Incident:* {inc['title']}\n*Damage:* {inc['the_damage']}\n*Status:* {inc['status']}\n\n*Live Radar:* AI DarkWatch"
        encoded_msg = urllib.parse.quote(msg_text)
        wa_url = f"https://wa.me/?text={encoded_msg}"
        
        st.markdown(f"""
        <div class="metric-card" style="margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <strong style="font-size: 14px; color: #ffffff;">{inc['title']}</strong>
                <span class="badge-critical">{inc['severity']}</span>
            </div>
            <div style="font-size: 12px; color: #94a3b8; margin: 4px 0;">🏢 {inc['company']} • 📅 {inc['date']}</div>
            <ul style="font-size: 12.5px; color: #cbd5e1; margin: 6px 0 10px 18px;">
                <li><strong>What Happened:</strong> {inc['what_happened']}</li>
                <li><strong>The Damage:</strong> {inc['the_damage']}</li>
                <li><strong>Status:</strong> {inc['status']}</li>
            </ul>
            <a href="{wa_url}" target="_blank" class="wa-btn">
                💬 Send to WhatsApp
            </a>
        </div>
        """, unsafe_allow_html=True)

# Footer & Deployment Info
st.markdown("---")
with st.expander("🌐 How to Deploy to Streamlit Community Cloud (Free)"):
    st.markdown("""
    1. **Push your code to GitHub**:
       ```bash
       git remote add origin https://github.com/<YOUR_USERNAME>/ai-darkwatch.git
       git push -u origin main
       ```
    2. Visit **[share.streamlit.io](https://share.streamlit.io)** and log in with GitHub.
    3. Click **"New App"** -> choose repository `ai-darkwatch` -> file `app.py`.
    4. Click **Deploy!** Your app will be live globally at `https://<your-app>.streamlit.app`.
    """)
