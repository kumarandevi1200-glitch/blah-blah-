import reflex as rx


def hero_defense_hub():
    """
    Signature Multi-Pillar Cyber Defense HUD Component.
    Visually showcases all 3 core capabilities of the platform:
    1. Voice Deepfake Spectral Scanner
    2. Text & SMS Phishing RAG Engine
    3. Suspect Intelligence & Threat Registry
    """
    return rx.html(
        """
        <div style="width: 100%; max-width: 980px; margin: 0 auto; text-align: center;">
            <style>
                @keyframes waveMorph {
                    0% {
                        d: path("M 10 30 Q 50 5, 90 30 T 170 30 T 250 30");
                        stroke: #38BDF8;
                        filter: drop-shadow(0 0 6px rgba(56, 189, 248, 0.6));
                    }
                    50% {
                        d: path("M 10 30 Q 30 2, 60 55 T 130 5 T 250 30");
                        stroke: #EF4444;
                        filter: drop-shadow(0 0 10px rgba(239, 68, 68, 0.8));
                    }
                    100% {
                        d: path("M 10 30 Q 50 5, 90 30 T 170 30 T 250 30");
                        stroke: #38BDF8;
                        filter: drop-shadow(0 0 6px rgba(56, 189, 248, 0.6));
                    }
                }
                .hero-wave-path {
                    animation: waveMorph 4s ease-in-out infinite;
                }
                
                @keyframes pulseScan {
                    0% { opacity: 0.3; transform: scaleX(0.95); }
                    50% { opacity: 1; transform: scaleX(1.02); }
                    100% { opacity: 0.3; transform: scaleX(0.95); }
                }
                .scan-bar-pulse {
                    animation: pulseScan 3s ease-in-out infinite;
                }

                @keyframes radarPing {
                    0% { r: 4px; opacity: 1; }
                    100% { r: 24px; opacity: 0; }
                }
                .radar-ring {
                    animation: radarPing 2.5s cubic-bezier(0, 0.2, 0.8, 1) infinite;
                }

                .pillar-card {
                    transition: all 0.3s ease;
                }
                .pillar-card:hover {
                    transform: translateY(-4px);
                    border-color: rgba(56, 189, 248, 0.5) !important;
                    box-shadow: 0 8px 24px rgba(16, 185, 129, 0.15);
                }
            </style>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-top: 12px; max-width: 100%; box-sizing: border-box;">
                
                <!-- Pillar 1: Voice Deepfake Scanner -->
                <div class="pillar-card" style="background: rgba(10, 31, 46, 0.75); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 12px; padding: 20px; text-align: left; position: relative; overflow: hidden; backdrop-filter: blur(10px);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                        <span style="display: flex; align-items: center; gap: 8px; font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 15px; color: #F0F4F3;">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="22"/></svg>
                            Voice Deepfake AI
                        </span>
                        <span style="font-family: 'IBM Plex Mono', monospace; font-size: 10px; background: rgba(56, 189, 248, 0.15); color: #38BDF8; padding: 3px 8px; border-radius: 12px; font-weight: 600;">ACTIVE SCAN</span>
                    </div>
                    
                    <svg width="100%" height="45" viewBox="0 0 260 50" fill="none">
                        <line x1="0" y1="30" x2="260" y2="30" stroke="rgba(255,255,255,0.08)" stroke-dasharray="4 4"/>
                        <path class="hero-wave-path" d="M 10 30 Q 50 5, 90 30 T 170 30 T 250 30" fill="none" stroke-width="3" stroke-linecap="round"/>
                    </svg>

                    <div style="font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: rgba(240, 244, 243, 0.7); margin-top: 8px; display: flex; justify-content: space-between;">
                        <span>HF Speach-Agent</span>
                        <span style="color: #10B981; font-weight: 600;">99.2% Accuracy</span>
                    </div>
                </div>

                <!-- Pillar 2: SMS & Text Phishing RAG -->
                <div class="pillar-card" style="background: rgba(10, 31, 46, 0.75); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 12px; padding: 20px; text-align: left; position: relative; overflow: hidden; backdrop-filter: blur(10px);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                        <span style="display: flex; align-items: center; gap: 8px; font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 15px; color: #F0F4F3;">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                            Text Phishing RAG
                        </span>
                        <span style="font-family: 'IBM Plex Mono', monospace; font-size: 10px; background: rgba(16, 185, 129, 0.15); color: #10B981; padding: 3px 8px; border-radius: 12px; font-weight: 600;">LLAMA 3.3 RAG</span>
                    </div>
                    
                    <div class="scan-bar-pulse" style="background: rgba(16, 185, 129, 0.1); border: 1px border-box rgba(16, 185, 129, 0.3); border-radius: 6px; padding: 8px 10px; font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: #A7F3D0; margin: 4px 0 10px 0; height: 42px; display: flex; align-items: center; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                        ⚡ Urgent: Account suspended. Click http://bank-verify.cx...
                    </div>

                    <div style="font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: rgba(240, 244, 243, 0.7); display: flex; justify-content: space-between;">
                        <span>SMS / Whatsapp Scams</span>
                        <span style="color: #EF4444; font-weight: 600;">Urgency Tactics</span>
                    </div>
                </div>

                <!-- Pillar 3: Suspect Intelligence DB -->
                <div class="pillar-card" style="background: rgba(10, 31, 46, 0.75); border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 12px; padding: 20px; text-align: left; position: relative; overflow: hidden; backdrop-filter: blur(10px);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                        <span style="display: flex; align-items: center; gap: 8px; font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 15px; color: #F0F4F3;">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#F59E0B" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                            Suspect Threat DB
                        </span>
                        <span style="font-family: 'IBM Plex Mono', monospace; font-size: 10px; background: rgba(245, 158, 11, 0.15); color: #F59E0B; padding: 3px 8px; border-radius: 12px; font-weight: 600;">UPI / PHONE LOOKUP</span>
                    </div>

                    <div style="display: flex; align-items: center; gap: 12px; height: 42px; margin: 4px 0 10px 0;">
                        <svg width="40" height="40" viewBox="0 0 40 40">
                            <circle cx="20" cy="20" r="18" fill="none" stroke="rgba(245, 158, 11, 0.2)" stroke-width="2"/>
                            <circle class="radar-ring" cx="20" cy="20" r="4" fill="none" stroke="#F59E0B" stroke-width="2"/>
                            <circle cx="20" cy="20" r="4" fill="#F59E0B"/>
                        </svg>
                        <div style="font-family: 'IBM Plex Mono', monospace; font-size: 11px;">
                            <div style="color: #F0F4F3; font-weight: 600;">Flagged: +91 98765-XXXXX</div>
                            <div style="color: #F59E0B;">UPI: scammer@paytm</div>
                        </div>
                    </div>

                    <div style="font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: rgba(240, 244, 243, 0.7); display: flex; justify-content: space-between;">
                        <span>Central Intelligence</span>
                        <span style="color: #F59E0B; font-weight: 600;">Risk Score: 92/100</span>
                    </div>
                </div>

            </div>
        </div>
        """
    )


def live_animated_waveform():
    """Fallback waveform component preserved for backwards compatibility."""
    return hero_defense_hub()


def hero() -> rx.Component:
    """
    Comprehensive Hero Section Component.
    Portrays the entire Multi-Agent Platform: Voice Deepfakes, Text Scam RAG, Suspect Intelligence, and AI Assistant.
    """
    return rx.box(
        rx.box(
            rx.vstack(
                # Top Multi-Agent Platform Status Badge
                rx.hstack(
                    rx.box(
                        width="8px",
                        height="8px",
                        border_radius="50%",
                        background="#10B981",
                        box_shadow="0 0 10px #10B981",
                    ),
                    rx.text(
                        "Multi-Agent AI Defense Suite Active",
                        font_size="12px",
                        font_weight="700",
                        color="#F0F4F3",
                        font_family="'IBM Plex Mono', monospace",
                        user_select="none",
                    ),
                    rx.box(
                        "•",
                        color="rgba(240, 244, 243, 0.4)",
                        font_size="12px",
                    ),
                    rx.text(
                        "Voice • Text RAG • Suspect DB • AI Assistant",
                        font_size="11px",
                        font_weight="500",
                        color="rgba(56, 189, 248, 0.9)",
                        font_family="'IBM Plex Mono', monospace",
                        user_select="none",
                    ),
                    spacing="2",
                    align="center",
                    padding_x="14px",
                    padding_y="7px",
                    background="rgba(27, 110, 91, 0.35)",
                    border="1px solid rgba(27, 110, 91, 0.6)",
                    border_radius="20px",
                    backdrop_filter="blur(8px)",
                ),
                
                # Main Headline & Subtitle reflecting the WHOLE project
                rx.heading(
                    "All-in-One AI Platform Against Cyber Fraud",
                    font_size={"initial": "30px", "sm": "42px", "md": "52px"},
                    font_weight="800",
                    color="#F0F4F3",
                    font_family="'Space Grotesk', sans-serif",
                    text_align="center",
                    line_height="1.15",
                    max_width="980px",
                    margin_top="16px",
                    user_select="none",
                ),
                rx.text(
                    "Institutional multi-agent intelligence fighting voice cloning deepfakes, SMS phishing scams, fraudulent UPI/bank accounts, and cyber threats in real-time.",
                    font_size={"initial": "15px", "sm": "18px", "md": "19px"},
                    color="rgba(240, 244, 243, 0.85)",
                    font_family="'Outfit', sans-serif",
                    text_align="center",
                    max_width="820px",
                    margin_top="12px",
                    user_select="none",
                ),

                # Signature 3-Pillar Defense Hub Visual
                rx.box(
                    hero_defense_hub(),
                    width="100%",
                    margin_y="28px",
                ),
                
                # Call to Action Buttons covering all pillars
                rx.hstack(
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.icon("mic", size=18),
                                rx.text("Scan Voice Call"),
                                spacing="2",
                            ),
                            size="3",
                            background="#1B6E5B",
                            color="#F0F4F3",
                            font_weight="700",
                            font_family="'Space Grotesk', sans-serif",
                            padding_x="24px",
                            padding_y="22px",
                            border_radius="8px",
                            cursor="pointer",
                            box_shadow="0 4px 14px rgba(27, 110, 91, 0.4)",
                            _hover={"background": "#145C46", "transform": "translateY(-2px)"},
                        ),
                        href="/scan",
                        text_decoration="none",
                    ),
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.icon("shield-alert", size=18),
                                rx.text("Check Suspect DB / Text Scam"),
                                spacing="2",
                            ),
                            size="3",
                            background="rgba(56, 189, 248, 0.15)",
                            color="#38BDF8",
                            border="1px solid rgba(56, 189, 248, 0.4)",
                            font_weight="700",
                            font_family="'Space Grotesk', sans-serif",
                            padding_x="24px",
                            padding_y="22px",
                            border_radius="8px",
                            cursor="pointer",
                            _hover={"background": "rgba(56, 189, 248, 0.25)", "transform": "translateY(-2px)"},
                        ),
                        href="/suspect-intelligence",
                        text_decoration="none",
                    ),
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.icon("book-open", size=18),
                                rx.text("Help & Docs"),
                                spacing="2",
                            ),
                            size="3",
                            variant="outline",
                            color="#F0F4F3",
                            border="1px solid rgba(240, 244, 243, 0.3)",
                            font_weight="600",
                            font_family="'Space Grotesk', sans-serif",
                            padding_x="20px",
                            padding_y="22px",
                            border_radius="8px",
                            cursor="pointer",
                            _hover={"background": "rgba(255,255,255,0.08)", "transform": "translateY(-2px)"},
                        ),
                        href="/docs",
                        text_decoration="none",
                    ),
                    spacing="3",
                    align="center",
                    justify="center",
                    wrap="wrap",
                    margin_top="16px",
                ),
                
                # Bottom Full Platform Tech Architecture Strip
                rx.grid(
                    rx.box(
                        rx.vstack(
                            rx.text("VOICE ENGINE", font_size="10px", color="rgba(240, 244, 243, 0.5)", font_family="'IBM Plex Mono', monospace"),
                            rx.text("Mitran14 + Groq Whisper", font_size="12px", font_weight="700", color="#38BDF8", font_family="'IBM Plex Mono', monospace"),
                            spacing="0",
                            align="center",
                        ),
                        padding="12px 18px",
                        background="rgba(10, 31, 46, 0.6)",
                        border="1px solid rgba(56, 189, 248, 0.3)",
                        border_radius="8px",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("TEXT & RAG ENGINE", font_size="10px", color="rgba(240, 244, 243, 0.5)", font_family="'IBM Plex Mono', monospace"),
                            rx.text("Llama 3.3 70B Threat KB", font_size="12px", font_weight="700", color="#10B981", font_family="'IBM Plex Mono', monospace"),
                            spacing="0",
                            align="center",
                        ),
                        padding="12px 18px",
                        background="rgba(10, 31, 46, 0.6)",
                        border="1px solid rgba(16, 185, 129, 0.3)",
                        border_radius="8px",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("SUSPECT REGISTRY", font_size="10px", color="rgba(240, 244, 243, 0.5)", font_family="'IBM Plex Mono', monospace"),
                            rx.text("UPI / Phone Risk Score", font_size="12px", font_weight="700", color="#F59E0B", font_family="'IBM Plex Mono', monospace"),
                            spacing="0",
                            align="center",
                        ),
                        padding="12px 18px",
                        background="rgba(10, 31, 46, 0.6)",
                        border="1px solid rgba(245, 158, 11, 0.3)",
                        border_radius="8px",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("SYSTEM PERFORMANCE", font_size="10px", color="rgba(240, 244, 243, 0.5)", font_family="'IBM Plex Mono', monospace"),
                            rx.text("< 1.8s Real-Time Latency", font_size="12px", font_weight="700", color="#A7F3D0", font_family="'IBM Plex Mono', monospace"),
                            spacing="0",
                            align="center",
                        ),
                        padding="12px 18px",
                        background="rgba(10, 31, 46, 0.6)",
                        border="1px solid rgba(167, 243, 208, 0.3)",
                        border_radius="8px",
                    ),
                    columns=rx.breakpoints(initial="1", sm="2", md="4"),
                    spacing="3",
                    width="100%",
                    max_width="980px",
                    margin_top="28px",
                ),
                spacing="4",
                align="center",
                padding_y={"initial": "40px", "sm": "60px", "md": "70px"},
            ),
            max_width="100%",
            padding_x={"initial": "16px", "md": "32px"},
        ),
        background="linear-gradient(135deg, #061521 0%, #0A2E30 50%, #0F3D3E 100%)",
        border_bottom="3px solid #1B6E5B",
        position="relative",
        overflow="hidden",
        width="100%",
    )
