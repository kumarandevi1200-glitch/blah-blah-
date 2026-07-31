import reflex as rx
from cyber_shield_reflex.components import (
    header,
    hero,
    analysis_panel,
    how_it_works,
    architecture,
    footer,
    bot_agent,
    suspect_intelligence,
    faq,
)


def index() -> rx.Component:
    """Home Page Component (Landing overview stretched full-screen)."""
    return rx.box(
        header(),
        hero(),
        how_it_works(),
        faq(),
        footer(),
        bot_agent(),
        background="#F7F9F8",
        min_height="100vh",
        width="100%",
        font_family="'Outfit', sans-serif",
    )


def scan_page() -> rx.Component:
    """Report Voice Fraud & Live Scanner Page."""
    return rx.box(
        header(),
        analysis_panel(),
        footer(),
        bot_agent(),
        background="#F7F9F8",
        min_height="100vh",
        width="100%",
        font_family="'Outfit', sans-serif",
    )


def model_insights_page() -> rx.Component:
    """Model Insights & Architecture Page."""
    return rx.box(
        header(),
        architecture(),
        footer(),
        bot_agent(),
        background="#F7F9F8",
        min_height="100vh",
        width="100%",
        font_family="'Outfit', sans-serif",
    )


def suspect_intelligence_page() -> rx.Component:
    """Suspect Intelligence Database & Text Agent Scanner Page."""
    return rx.box(
        header(),
        suspect_intelligence(),
        footer(),
        bot_agent(),
        background="#F7F9F8",
        min_height="100vh",
        width="100%",
        font_family="'Outfit', sans-serif",
    )


def volunteers_page() -> rx.Component:
    """Volunteers & Contributor Network Page."""
    return rx.box(
        header(),
        rx.box(
            rx.vstack(
                rx.heading("Volunteers & Contributor Community", font_size="32px", font_weight="800", color="#0A1F2E", font_family="'Space Grotesk', sans-serif"),
                rx.text("Join security researchers, data scientists, and developers building open-source AI fraud defense.", font_size="16px", color="#5A6E72"),
                rx.box(
                    rx.vstack(
                        rx.heading("How to Contribute", font_size="20px", font_weight="700", color="#1B6E5B"),
                        rx.text("1. Submit voice sample datasets of synthetic vs natural callers to train models."),
                        rx.text("2. Report novel SMS phishing templates to enhance our Llama 3.3 threat prompt engine."),
                        rx.text("3. Integrate regional language whisper fine-tunes for local cybercrime defense."),
                        spacing="3",
                        align="start",
                    ),
                    padding="32px",
                    background="#FFFFFF",
                    border="1px solid #E2E8F0",
                    border_radius="12px",
                    width="100%",
                    margin_top="24px",
                ),
                padding_y="60px",
                align="start",
                width="100%",
            ),
            width="100%",
            padding_x={"initial": "16px", "md": "48px"},
        ),
        footer(),
        bot_agent(),
        background="#F7F9F8",
        min_height="100vh",
        width="100%",
        font_family="'Outfit', sans-serif",
    )


def docs_page() -> rx.Component:
    """Help & Documentation Page."""
    return rx.box(
        header(),
        architecture(),
        faq(),
        footer(),
        bot_agent(),
        background="#F7F9F8",
        min_height="100vh",
        width="100%",
        font_family="'Outfit', sans-serif",
    )


# App configuration with custom Google Fonts and clean global styles
app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@600;700;800&family=IBM+Plex Mono:wght@400;600;700&display=swap",
    ],
    style={
        "font_family": "'Outfit', sans-serif",
        "color": "#0D1B1E",
        "user_select": "none",
        "cursor": "default",
        "::selection": {
            "background": "#1B6E5B",
            "color": "#FFFFFF",
        },
    },
)

# Multi-Page Routes
app.add_page(index, route="/", title="Cyber Fraud Shield | Home")
app.add_page(scan_page, route="/scan", title="Cyber Fraud Shield | Report & Scan")
app.add_page(suspect_intelligence_page, route="/suspect-intelligence", title="Cyber Fraud Shield | Suspect Intelligence")
app.add_page(model_insights_page, route="/model-insights", title="Cyber Fraud Shield | Model Insights")
app.add_page(volunteers_page, route="/volunteers", title="Cyber Fraud Shield | Volunteers")
app.add_page(docs_page, route="/docs", title="Cyber Fraud Shield | Help & Docs")
