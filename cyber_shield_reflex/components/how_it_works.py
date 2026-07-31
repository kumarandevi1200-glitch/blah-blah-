import reflex as rx


def step_card(num: str, title: str, subtitle: str, icon_name: str):
    """Pipeline step card with numbered badge."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.text(num, font_size="14px", font_weight="800", color="#FFFFFF", font_family="'IBM Plex Mono', monospace"),
                    padding="6px 12px",
                    background="#1B6E5B",
                    border_radius="6px",
                ),
                rx.icon(icon_name, size=24, color="#1B6E5B"),
                justify="between",
                align="center",
                width="100%",
            ),
            rx.heading(title, font_size="17px", font_weight="700", color="#0A1F2E", font_family="'Space Grotesk', sans-serif", margin_top="12px"),
            rx.text(subtitle, font_size="13px", color="#5A6E72", font_family="'Inter', sans-serif", line_height="1.5"),
            spacing="2",
            align="start",
        ),
        padding="24px",
        background="#FFFFFF",
        border="1px solid #E2E8F0",
        border_radius="12px",
        box_shadow="0 4px 12px rgba(10, 31, 46, 0.03)",
        _hover={"border_color": "#1B6E5B", "transform": "translateY(-2px)"},
        transition="all 0.2s ease",
        height="100%",
    )


def how_it_works() -> rx.Component:
    """
    How It Works 4-step pipeline component.
    """
    return rx.box(
        rx.container(
            rx.vstack(
                rx.vstack(
                    rx.text("PIPELINE ARCHITECTURE", font_size="11px", font_weight="700", color="#1B6E5B", font_family="'IBM Plex Mono', monospace", letter_spacing="0.1em"),
                    rx.heading("How Cyber Fraud Shield Verifies Voice Calls", font_size="28px", font_weight="800", color="#0A1F2E", font_family="'Space Grotesk', sans-serif"),
                    rx.text("End-to-end multi-agent evaluation pipeline running under 2 seconds.", font_size="15px", color="#5A6E72", font_family="'Inter', sans-serif"),
                    spacing="1",
                    align="center",
                    text_align="center",
                ),
                
                rx.grid(
                    step_card(
                        "1",
                        "Audio In",
                        "Accepts call recordings, voice notes (.wav, .mp3, .m4a) or raw text payloads directly into the processing queue.",
                        "upload",
                    ),
                    step_card(
                        "2",
                        "Feature Extraction",
                        "Calculates spectral centroid, pitch stability std dev, and transcribes spoken audio via Groq Whisper Large v3.",
                        "activity",
                    ),
                    step_card(
                        "3",
                        "Model Inference",
                        "Queries custom Hugging Face classifier (Mitran14/speach-agent) and TF-IDF Logistic Regression scam model.",
                        "cpu",
                    ),
                    step_card(
                        "4",
                        "Executive Verdict",
                        "Generates synthetic confidence score %, threat classification, and emergency banking action playbooks.",
                        "shield-check",
                    ),
                    columns=rx.breakpoints(initial="1", sm="2", md="4"),
                    spacing="5",
                    margin_top="32px",
                    width="100%",
                ),
                spacing="4",
                align="center",
                padding_y="60px",
            ),
            max_width="100%",
            padding_x="32px",
        ),
        background="#FFFFFF",
        border_bottom="1px solid #E2E8F0",
    )
