import streamlit as st
import os
import json
import time

# Page config
st.set_page_config(
    page_title="Cyber Fraud Shield AI Assistant",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for rich cybersecurity aesthetics, glassmorphism, dark theme & dynamic visual badges
st.markdown("""
<style>
    /* Global Styles */
    .stApp {
        background-color: #0b0f19;
        color: #e2e8f0;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Header Container */
    .cyber-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
        border: 1px solid rgba(99, 102, 241, 0.3);
        border-radius: 16px;
        padding: 24px 32px;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }
    
    .cyber-title {
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin: 0;
    }
    
    .cyber-subtitle {
        color: #94a3b8;
        font-size: 1rem;
        margin-top: 6px;
    }
    
    /* Glassmorphism Card */
    .glass-card {
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
    }
    
    /* Threat Badges */
    .badge-safe {
        background-color: rgba(16, 185, 129, 0.15);
        color: #10b981;
        border: 1px solid #10b981;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 700;
    }
    .badge-caution {
        background-color: rgba(245, 158, 11, 0.15);
        color: #f59e0b;
        border: 1px solid #f59e0b;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 700;
    }
    .badge-high {
        background-color: rgba(239, 68, 68, 0.15);
        color: #ef4444;
        border: 1px solid #ef4444;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 700;
    }
    .badge-critical {
        background-color: rgba(225, 29, 72, 0.25);
        color: #f43f5e;
        border: 2px solid #f43f5e;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: 800;
        animation: pulse 1.8s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(244, 63, 94, 0.4); }
        70% { box-shadow: 0 0 0 10px rgba(244, 63, 94, 0); }
        100% { box-shadow: 0 0 0 0 rgba(244, 63, 94, 0); }
    }
    
    /* Stat Metric Box */
    .metric-box {
        background: #1e293b;
        border-radius: 10px;
        padding: 16px;
        text-align: center;
        border: 1px solid #334155;
    }
    
    .metric-val {
        font-size: 2rem;
        font-weight: 800;
        color: #38bdf8;
    }
    
    .metric-lbl {
        font-size: 0.85rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Code / Guide highlight */
    .guide-box {
        background: #0f172a;
        border-left: 4px solid #38bdf8;
        padding: 16px;
        border-radius: 0 8px 8px 0;
        margin: 12px 0;
    }
</style>
""", unsafe_allow_html=True)

# Imports after page config
from src.config import Config, EMERGENCY_PLAYBOOKS
from src.agents.orchestrator import FreeAgentOrchestrator

# Initialize Orchestrator in session state
if "orchestrator" not in st.session_state:
    st.session_state.orchestrator = FreeAgentOrchestrator()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

orchestrator = st.session_state.orchestrator

# Header Banner
st.markdown("""
<div class="cyber-header">
    <div class="cyber-title">🛡️ Cyber Fraud Shield AI Assistant</div>
    <div class="cyber-subtitle">Multi-Agent AI Defense Platform • Voice & Text Scam Detection • Cyber Security Emergency Bot</div>
</div>
""", unsafe_allow_html=True)

# Sidebar System Controls
with st.sidebar:
    st.image("https://img.icons8.com/isometric/96/shield.png", width=70)
    st.title("System Status")
    
    active_mode = Config.active_mode()
    if "Free API" in active_mode:
        st.success(f"🟢 {active_mode}")
    else:
        st.info(f"⚡ {active_mode}")
        
    st.markdown("---")
    st.subheader("Free API Configurations")
    
    st.markdown("**1. Groq Free API:** " + ("✅ Connected" if Config.GROQ_API_KEY else "❌ Unset (Using Heuristic Engine)"))
    st.markdown("**2. HuggingFace Token:** " + ("✅ Connected" if Config.HUGGINGFACE_API_KEY else "❌ Unset"))
    st.markdown("**3. Gemini Free API:** " + ("✅ Connected" if Config.GEMINI_API_KEY else "❌ Unset"))
    
    st.markdown("---")
    st.markdown("### 🚨 Emergency Hotlines")
    st.warning("**India National Cyber Hotline:** `1930`\n\n**Report Cyber Crime Portal:** `cybercrime.gov.in`")

# Navigation Tabs
tab_bot, tab_speech, tab_text, tab_guide = st.tabs([
    "🤖 Cyber Shield Bot (AI Assistant)",
    "🎙️ Speech & Voice AI Scanner",
    "🔍 Text Scam Scanner",
    "📚 Free AI Agents & Setup Instructions"
])

# ==========================================
# TAB 1: CYBER SHIELD BOT (AI ASSISTANT)
# ==========================================
with tab_bot:
    st.markdown("### 🤖 Cyber Shield Emergency Assistant")
    st.caption("Ask questions about suspicious callers, security threats, or click quick emergency action buttons below.")

    # Quick Emergency Action Buttons
    st.markdown("**🚨 Quick Emergency Protocols:**")
    col1, col2, col3, col4 = st.columns(4)
    
    quick_prompt = None
    with col1:
        if st.button("🔑 Shared OTP / PIN", use_container_width=True):
            quick_prompt = "I mistakenly shared my bank OTP with a caller!"
    with col2:
        if st.button("🌐 Clicked Fake Link", use_container_width=True):
            quick_prompt = "I clicked a suspicious link from an SMS message."
    with col3:
        if st.button("📞 Fake Police/Customs Call", use_container_width=True):
            quick_prompt = "I got a call claiming to be customs saying a illegal package is in my name."
    with col4:
        if st.button("💸 Money Transferred Scam", use_container_width=True):
            quick_prompt = "I transferred money to a scammer, how do I recover funds?"

    st.markdown("---")

    # Render Chat History
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # Handle user input or quick prompt
    user_input = st.chat_input("Describe the suspicious incident or ask for advice...")
    active_prompt = quick_prompt or user_input

    if active_prompt:
        # Append User Message
        st.session_state.chat_history.append({"role": "user", "content": active_prompt})
        with st.chat_message("user"):
            st.markdown(active_prompt)

        # Generate Bot Response using CyberShieldBotAgent
        with st.chat_message("assistant"):
            with st.spinner("Cyber Shield Bot is analyzing threat parameters..."):
                response_text = orchestrator.bot_agent.respond(active_prompt, st.session_state.chat_history)
                st.markdown(response_text)
                st.session_state.chat_history.append({"role": "assistant", "content": response_text})

# ==========================================
# TAB 2: SPEECH & VOICE AI SCANNER
# ==========================================
with tab_speech:
    st.markdown("### 🎙️ Speech & AI Voice Spoof Scanner")
    st.caption("Upload or record audio clips to transcribe speech and detect AI-cloned / synthetic voice signatures.")

    col_up, col_info = st.columns([1.2, 1])

    with col_up:
        uploaded_file = st.file_uploader("Upload suspicious voice recording or call audio (.wav, .mp3, .m4a, .ogg)", type=["wav", "mp3", "m4a", "ogg"])
        
        st.markdown("**OR Try Built-in Test Sample Voice Clips:**")
        sample_choice = st.selectbox("Select sample test case:", [
            "None (Upload own file above)",
            "Sample 1: Fake Bank Urgent OTP Call",
            "Sample 2: Customs Seizure Threats (Impersonation)",
            "Sample 3: Family Emergency Impersonation Scam"
        ])

    with col_info:
        st.info("""
        **How Speech Analysis Works:**
        - **Whisper Speech-to-Text:** Transcribes spoken audio into full text transcripts.
        - **Synthetic Voice Detector:** Evaluates spectral micro-variations, pitch stability, and acoustic artifacts to catch deepfake/cloned voice audio.
        - **Fraud Content Engine:** Scans transcribed text for scam indicators.
        """)

    if uploaded_file is not None or sample_choice != "None (Upload own file above)":
        if st.button("🚀 Run Speech & Voice Spoof Analysis", type="primary", use_container_width=True):
            with st.spinner("Transcribing speech and running voice acoustic analysis..."):
                if uploaded_file is not None:
                    audio_bytes = uploaded_file.read()
                    fname = uploaded_file.name
                else:
                    audio_bytes = sample_choice.encode("utf-8")
                    fname = f"{sample_choice.replace(' ', '_').lower()}.wav"
                
                result = orchestrator.speech_agent.analyze_audio(audio_bytes, fname)
                
                st.markdown("---")
                st.markdown("### 📊 Voice Analysis Results")
                
                res_col1, res_col2, res_col3 = st.columns(3)
                with res_col1:
                    st.markdown(f"""
                    <div class="metric-box">
                        <div class="metric-val">{result['overall_voice_risk_score']}/100</div>
                        <div class="metric-lbl">Overall Voice Threat Score</div>
                    </div>
                    """, unsafe_allow_html=True)
                with res_col2:
                    is_synth = result['voice_spoof_metrics']['is_synthetic']
                    badge_class = "badge-critical" if is_synth else "badge-safe"
                    st.markdown(f"""
                    <div class="metric-box">
                        <div style="font-size: 1.3rem; margin-top:4px;" class="{badge_class}">{result['voice_spoof_metrics']['voice_nature']}</div>
                        <div class="metric-lbl" style="margin-top:10px;">Voice Classification</div>
                    </div>
                    """, unsafe_allow_html=True)
                with res_col3:
                    st.markdown(f"""
                    <div class="metric-box">
                        <div class="metric-val">{result['voice_spoof_metrics']['synthetic_confidence']}%</div>
                        <div class="metric-lbl">AI Synthetic Confidence</div>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown("#### 📝 Speech-to-Text Transcription")
                st.code(result["transcription"], language="text")
                st.caption(f"Engine: {result['transcription_engine']}")

                st.markdown("#### 🔬 Acoustic Voice Artifact Inspection")
                st.json(result["voice_spoof_metrics"])

# ==========================================
# TAB 3: TEXT SCAM SCANNER
# ==========================================
with tab_text:
    st.markdown("### 🔍 Text Scam & Phishing Scanner")
    st.caption("Scan suspicious SMS messages, WhatsApp chats, emails, or call transcripts for scam indicators.")

    sample_texts = {
        "Custom": "",
        "Bank OTP Scam": "URGENT: Your HDFC bank account ending in 4921 has been blocked due to missing KYC. Click http://hdfc-verify-update.com immediately to unblock within 24 hours.",
        "Courier Scam": "FedEx Express: Package #IND9841 could not be delivered due to unpaid customs fee of $5. Pay now at http://bit.ly/fedex-custom-pay or parcel will be returned.",
        "Prize/Lottery Scam": "Congratulations! You have won $50,000 in the Amazon International Lucky Draw. Reply with your bank account number and UPI ID to claim your prize."
    }

    selected_sample = st.selectbox("Load sample threat text:", list(sample_texts.keys()))
    default_text = sample_texts[selected_sample] if selected_sample != "Custom" else ""

    input_text = st.text_area("Paste suspicious text / email content below:", value=default_text, height=140, placeholder="Paste SMS, WhatsApp message, or email here...")

    if st.button("🔍 Scan Text For Fraud", type="primary", use_container_width=True):
        if not input_text.strip():
            st.warning("Please paste some text to scan.")
        else:
            with st.spinner("Text Scam Detector Agent analyzing message patterns..."):
                analysis = orchestrator.text_agent.analyze(input_text)

                st.markdown("---")
                st.markdown("### 📋 Scam Analysis Report")

                col_a, col_b = st.columns([1, 1.8])

                with col_a:
                    st.metric("Threat Risk Score", f"{analysis['risk_score']} / 100")
                    st.markdown(f"**Threat Classification:** {analysis['threat_level']}")
                    st.markdown(f"**Scam Category:** `{analysis['scam_type']}`")
                    st.caption(f"Engine: {analysis.get('engine_used', 'Heuristic')}")

                with col_b:
                    st.markdown("**Matched Scam Tactics & Red Flags:**")
                    for flag in analysis.get("matched_tactics", []):
                        st.markdown(f"- ⚠️ {flag}")
                    
                    st.markdown("**Key Warning Signs:**")
                    for sign in analysis.get("key_warning_signs", []):
                        st.markdown(f"- 🔴 {sign}")

                st.info(f"💡 **Actionable Advice:** {analysis.get('actionable_advice', '')}")

# ==========================================
# TAB 4: FREE AI AGENTS & SETUP GUIDE
# ==========================================
with tab_guide:
    st.markdown("### 📚 Free AI Keys & Agents Setup Guide")
    st.markdown("""
    This project is built to run 100% free using open-source models, free-tier AI APIs, and local fallback engines.
    Below is your complete step-by-step walkthrough to configure free API keys and understand the multi-agent architecture.
    """)

    st.markdown("---")
    st.markdown("### 🔑 Step 1: Acquiring 100% Free API Keys")

    st.markdown("""
    <div class="guide-box">
        <h4>1. Groq Free API (Recommended - Ultra Fast)</h4>
        <ul>
            <li><b>What it provides:</b> Free access to <code>Llama 3.3 70B Versatile</code> (LLM agent) and <code>Whisper Large v3</code> (voice transcription).</li>
            <li><b>Cost:</b> 100% Free with generous daily rate limits.</li>
            <li><b>How to get key:</b>
                <ol>
                    <li>Go to <a href="https://console.groq.com" target="_blank">console.groq.com</a></li>
                    <li>Sign up / log in with Google or GitHub.</li>
                    <li>Navigate to <b>API Keys</b> &rarr; Click <b>Create API Key</b>.</li>
                    <li>Copy key starting with <code>gsk_...</code></li>
                </ol>
            </li>
        </ul>
    </div>
    
    <div class="guide-box">
        <h4>2. Hugging Face Free Token</h4>
        <ul>
            <li><b>What it provides:</b> Free access to open-source speech, voice spoof, and NLP models.</li>
            <li><b>How to get key:</b>
                <ol>
                    <li>Go to <a href="https://huggingface.co/settings/tokens" target="_blank">huggingface.co/settings/tokens</a></li>
                    <li>Create a free account &rarr; Click <b>New Token</b> (Role: Read).</li>
                    <li>Copy key starting with <code>hf_...</code></li>
                </ol>
            </li>
        </ul>
    </div>

    <div class="guide-box">
        <h4>3. Google Gemini Free API Key</h4>
        <ul>
            <li><b>What it provides:</b> Free access to <code>Gemini 1.5 Flash</code> for advanced reasoning.</li>
            <li><b>How to get key:</b>
                <ol>
                    <li>Go to <a href="https://aistudio.google.com" target="_blank">aistudio.google.com</a></li>
                    <li>Click <b>Get API Key</b> &rarr; Create Key in new project.</li>
                </ol>
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🛠️ Step 2: Configuring Environment & Running the Web App")

    st.code("""
# 1. Open .env file or copy from .env.example
cp .env.example .env

# 2. Add your free API key in .env:
GROQ_API_KEY=gsk_your_free_groq_key_here

# 3. Launch the Streamlit Web Application:
streamlit run src/app.py
""", language="bash")

    st.markdown("---")
    st.markdown("### 🤖 Step 3: Multi-Agent Architecture Overview")
    st.markdown("""
    The application coordinates three dedicated AI agents:
    1. **Text Scam Detector Agent (`src/agents/text_agent.py`):** Uses heuristic threat rules + Llama-3.3-70B to detect social engineering and phishing tactics.
    2. **Speech & Voice Spoof Agent (`src/agents/speech_agent.py`):** Runs Whisper voice transcription + spectral acoustic artifact analysis for deepfake voice detection.
    3. **Cyber Shield Bot Agent (`src/agents/bot_agent.py`):** Interactive emergency advisor agent providing step-by-step banking freeze & cybercrime reporting playbooks.
    """)

# Footer
st.markdown("---")
st.caption("🛡️ Cyber Fraud Shield • Built for HackIndia • Open-Source & Free AI Powered")
