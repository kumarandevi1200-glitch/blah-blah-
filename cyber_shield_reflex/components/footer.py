import reflex as rx
from cyber_shield_reflex.state import State
from cyber_shield_reflex.components.modals import complaint_prerequisites_modal, disclaimer_modal


def chevron_item(label: str, href: str = "#", on_click=None) -> rx.Component:
    """Helper for footer links with chevron arrow indicator."""
    if on_click is not None:
        return rx.box(
            rx.hstack(
                rx.icon("chevron-right", size=16, color="#0284C7"),
                rx.text(label, font_size="14px", color="#334155", font_family="'Outfit', sans-serif"),
                spacing="1",
                align="center",
            ),
            cursor="pointer",
            on_click=on_click,
            _hover={"opacity": 0.8},
        )
    return rx.link(
        rx.hstack(
            rx.icon("chevron-right", size=16, color="#0284C7"),
            rx.text(label, font_size="14px", color="#334155", font_family="'Outfit', sans-serif"),
            spacing="1",
            align="center",
        ),
        href=href,
        text_decoration="none",
        _hover={"opacity": 0.8},
    )


def footer(show_helpline_ribbon: bool = False) -> rx.Component:
    """
    Official Cyber Crime Portal-styled Footer Component matching government design.
    show_helpline_ribbon: Set to True ONLY on the Home landing page.
    """
    return rx.box(
        complaint_prerequisites_modal(),
        disclaimer_modal(),
        
        # Upper Helpline & Complaint Action Ribbon (White background with blue accent - ONLY on Home page)
        rx.cond(
            show_helpline_ribbon,
            rx.box(
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Any victim of financial cyber fraud can dial helpline number 1930",
                            font_size="16px",
                            font_weight="600",
                            color="#0284C7",
                            font_family="'Outfit', sans-serif",
                        ),
                        rx.button(
                            "Register a Complaint",
                            background="linear-gradient(90deg, #00A3E0 0%, #0077C5 100%)",
                            color="#FFFFFF",
                            font_weight="700",
                            font_size="14px",
                            font_family="'Outfit', sans-serif",
                            padding_x="24px",
                            padding_y="12px",
                            border_radius="6px",
                            box_shadow="0 4px 12px rgba(0, 163, 224, 0.3)",
                            cursor="pointer",
                            on_click=State.toggle_complaint_modal,  # type: ignore
                            _hover={"opacity": 0.9},
                        ),
                        spacing="3",
                        align="start",
                    ),
                    width="100%",
                    padding_x={"initial": "16px", "md": "48px"},
                    padding_y="28px",
                ),
                background="#FFFFFF",
                border_bottom="1px solid #E2E8F0",
                width="100%",
            ),
        ),
        
        # Lower Footer Links & Official Government Contact Info (Light Icy Blue background)
        rx.box(
            rx.box(
                rx.grid(
                    # Col 1: Help & Support
                    rx.vstack(
                        rx.heading("Help & Support", font_size="18px", font_weight="700", color="#0F172A", font_family="'Space Grotesk', sans-serif", margin_bottom="8px"),
                        chevron_item("Feedback", href="/docs"),
                        chevron_item("Contact Us", href="#contact-us"),
                        chevron_item("FAQ", href="/docs#faq-section"),
                        spacing="2",
                        align="start",
                    ),
                    
                    # Col 2: Information
                    rx.vstack(
                        rx.heading("Information", font_size="18px", font_weight="700", color="#0F172A", font_family="'Space Grotesk', sans-serif", margin_bottom="8px"),
                        chevron_item("Website Policies", href="/docs"),
                        chevron_item("Privacy Policy", href="/docs"),
                        chevron_item("Disclaimer", on_click=State.toggle_disclaimer_modal),  # type: ignore
                        spacing="2",
                        align="start",
                    ),
                    
                    # Col 3: Contact Us (Official Government Contact Info)
                    rx.vstack(
                        rx.heading("Contact Us", font_size="18px", font_weight="700", color="#0F172A", font_family="'Space Grotesk', sans-serif", margin_bottom="8px"),
                        rx.hstack(
                            rx.icon("map-pin", size=18, color="#0284C7"),
                            rx.text(
                                "5th Floor, NDCC-II Building, Jai Singh Road, New Delhi",
                                font_size="14px",
                                color="#334155",
                                font_family="'Outfit', sans-serif",
                            ),
                            spacing="2",
                            align="start",
                        ),
                        rx.hstack(
                            rx.icon("mail", size=18, color="#0284C7"),
                            rx.vstack(
                                rx.text("cyberdost[at]mha[dot]gov[dot]in", font_size="14px", color="#334155", font_family="'Outfit', sans-serif"),
                                rx.text("aski4c-mha[at]nic[dot]in", font_size="14px", color="#334155", font_family="'Outfit', sans-serif"),
                                spacing="0",
                                align="start",
                            ),
                            spacing="2",
                            align="start",
                        ),
                        rx.hstack(
                            rx.icon("phone", size=18, color="#0284C7"),
                            rx.text(
                                "011-23438207 / 08 | Toll Free Helpline: 1930",
                                font_size="14px",
                                font_weight="600",
                                color="#0F172A",
                                font_family="'Outfit', sans-serif",
                            ),
                            spacing="2",
                            align="center",
                        ),
                        spacing="3",
                        align="start",
                    ),
                    columns=rx.breakpoints(initial="1", sm="2", md="3"),
                    spacing="6",
                    width="100%",
                ),
                width="100%",
                padding_x={"initial": "16px", "md": "48px"},
                padding_y="40px",
            ),
            background="#EBF8FF",
            border_top="1px solid #BAE6FD",
            width="100%",
            id="contact-us",
        ),
        width="100%",
    )
