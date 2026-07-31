import reflex as rx


def live_animated_waveform():
    """
    Signature Hero SVG Component.
    Builds a live morphing waveform representing the transition between
    Genuine Voice (smooth sine wave, sky blue) and Spoofed Cloned Voice (jagged, red).
    Uses pure CSS keyframe animation for high performance.
    """
    return rx.html(
        """
        <div style="width: 100%; max-width: 640px; margin: 0 auto; text-align: center;">
            <style>
                @keyframes waveMorph {
                    0% {
                        d: path("M 10 50 Q 60 10, 110 50 T 210 50 T 310 50 T 410 50 T 510 50 T 610 50");
                        stroke: #38BDF8;
                        filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.6));
                    }
                    50% {
                        d: path("M 10 50 Q 30 5, 60 85 T 140 15 T 220 90 T 330 10 T 450 80 T 610 50");
                        stroke: #C4432E;
                        filter: drop-shadow(0 0 12px rgba(196, 67, 46, 0.8));
                    }
                    100% {
                        d: path("M 10 50 Q 60 10, 110 50 T 210 50 T 310 50 T 410 50 T 510 50 T 610 50");
                        stroke: #38BDF8;
                        filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.6));
                    }
                }
                .waveform-path {
                    animation: waveMorph 5s ease-in-out infinite;
                }
            </style>
            <svg width="100%" height="100" viewBox="0 0 620 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Background Subtle Grid Lines -->
                <line x1="0" y1="50" x2="620" y2="50" stroke="rgba(255,255,255,0.08)" stroke-dasharray="4 4" />
                <line x1="0" y1="25" x2="620" y2="25" stroke="rgba(255,255,255,0.04)" stroke-dasharray="2 4" />
                <line x1="0" y1="75" x2="620" y2="75" stroke="rgba(255,255,255,0.04)" stroke-dasharray="2 4" />
                
                <!-- Animated Morphing Waveform Path -->
                <path class="waveform-path" d="M 10 50 Q 60 10, 110 50 T 210 50 T 310 50 T 410 50 T 510 50 T 610 50" fill="none" stroke-width="3.5" stroke-linecap="round" />
            </svg>
            <div style="display: flex; justify-content: space-between; font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: rgba(240, 244, 243, 0.6); margin-top: 4px; padding: 0 16px;">
                <span>0.00s (Sampling)</span>
                <span style="color: #38BDF8;">● Genuine Human Signature</span>
                <span style="color: #C4432E;">● AI Spoof Detected</span>
                <span>4.00s (Spectral FFT)</span>
            </div>
        </div>
        """
    )


def hero() -> rx.Component:
    """
    Hero Section Component with gradient, animated morphing waveform, CTAs, and status strip.
    """
    return rx.box(
        rx.box(
            rx.vstack(
                # Top Live Status Badge
                rx.hstack(
                    rx.hstack(
                        rx.box(
                            width="8px",
                            height="8px",
                            border_radius="50%",
                            background="#10B981",
                            box_shadow="0 0 10px #10B981",
                        ),
                        rx.text(
                            "Model Active: Mitran14/speach-agent",
                            font_size="12px",
                            font_weight="600",
                            color="#F0F4F3",
                            font_family="'IBM Plex Mono', monospace",
                            user_select="none",
                        ),
                        spacing="2",
                        align="center",
                        padding_x="12px",
                        padding_y="6px",
                        background="rgba(27, 110, 91, 0.4)",
                        border="1px solid rgba(27, 110, 91, 0.6)",
                        border_radius="20px",
                    ),
                    spacing="3",
                    align="center",
                ),
                
                # Signature Animated Waveform
                rx.box(
                    live_animated_waveform(),
                    width="100%",
                    margin_y="24px",
                ),
                
                # Main Headline & Subtitle
                rx.heading(
                    "Detect Voice Spoofing Before It Costs You",
                    font_size={"initial": "32px", "sm": "42px", "md": "54px"},
                    font_weight="800",
                    color="#F0F4F3",
                    font_family="'Space Grotesk', sans-serif",
                    text_align="center",
                    line_height="1.15",
                    max_width="950px",
                    user_select="none",
                ),
                rx.text(
                    "Institutional-grade AI platform for real-time cloned voice detection, synthetic call verification, and multi-agent cyber-fraud defense.",
                    font_size={"initial": "16px", "sm": "18px", "md": "20px"},
                    color="rgba(240, 244, 243, 0.85)",
                    font_family="'Outfit', sans-serif",
                    text_align="center",
                    max_width="780px",
                    margin_top="12px",
                    user_select="none",
                ),
                
                # Call to Action Buttons
                rx.hstack(
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.icon("shield-alert", size=18),
                                rx.text("Analyze a Call"),
                                spacing="2",
                            ),
                            size="3",
                            background="#1B6E5B",
                            color="#F0F4F3",
                            font_weight="700",
                            font_family="'Space Grotesk', sans-serif",
                            padding_x="28px",
                            padding_y="22px",
                            border_radius="8px",
                            cursor="pointer",
                            _hover={"background": "#145C46", "transform": "translateY(-1px)"},
                        ),
                        href="/scan",
                        text_decoration="none",
                    ),
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.icon("cpu", size=18),
                                rx.text("View Model Architecture"),
                                spacing="2",
                            ),
                            size="3",
                            variant="outline",
                            color="#F0F4F3",
                            border="1px solid rgba(240, 244, 243, 0.4)",
                            font_weight="600",
                            font_family="'Space Grotesk', sans-serif",
                            padding_x="24px",
                            padding_y="22px",
                            border_radius="8px",
                            cursor="pointer",
                            _hover={"background": "rgba(255,255,255,0.08)"},
                        ),
                        href="/model-insights",
                        text_decoration="none",
                    ),
                    spacing="4",
                    align="center",
                    margin_top="24px",
                ),
                
                # Bottom Stat Strip
                rx.hstack(
                    rx.box(
                        rx.vstack(
                            rx.text("HF MODEL", font_size="10px", color="rgba(240, 244, 243, 0.5)", font_family="'IBM Plex Mono', monospace"),
                            rx.text("Mitran14/speach-agent", font_size="13px", font_weight="700", color="#F0F4F3", font_family="'IBM Plex Mono', monospace"),
                            spacing="0",
                            align="center",
                        ),
                        padding="12px 24px",
                        background="rgba(10, 31, 46, 0.6)",
                        border="1px solid rgba(27, 110, 91, 0.4)",
                        border_radius="8px",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("INFERENCE LATENCY", font_size="10px", color="rgba(240, 244, 243, 0.5)", font_family="'IBM Plex Mono', monospace"),
                            rx.text("< 1.8s Real-time", font_size="13px", font_weight="700", color="#10B981", font_family="'IBM Plex Mono', monospace"),
                            spacing="0",
                            align="center",
                        ),
                        padding="12px 24px",
                        background="rgba(10, 31, 46, 0.6)",
                        border="1px solid rgba(27, 110, 91, 0.4)",
                        border_radius="8px",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("FAILOVER ENGINE", font_size="10px", color="rgba(240, 244, 243, 0.5)", font_family="'IBM Plex Mono', monospace"),
                            rx.text("Groq Whisper + Spectral FFT", font_size="13px", font_weight="700", color="#38BDF8", font_family="'IBM Plex Mono', monospace"),
                            spacing="0",
                            align="center",
                        ),
                        padding="12px 24px",
                        background="rgba(10, 31, 46, 0.6)",
                        border="1px solid rgba(27, 110, 91, 0.4)",
                        border_radius="8px",
                    ),
                    spacing="4",
                    align="center",
                    margin_top="36px",
                    display={"initial": "none", "md": "flex"},
                ),
                spacing="4",
                align="center",
                padding_y={"initial": "50px", "sm": "70px", "md": "90px"},
            ),
            max_width="100%",
            padding_x="32px",
        ),
        background="linear-gradient(135deg, #0A1F2E 0%, #0F3D3E 100%)",
        border_bottom="3px solid #1B6E5B",
        position="relative",
        overflow="hidden",
        width="100%",
    )
