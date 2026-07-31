import reflex as rx
from cyber_shield_reflex.state import State


def profile_table_row(label: str, val: rx.Var[str]) -> rx.Component:
    """Renders a single row in the user profile table."""
    return rx.table.row(
        rx.table.cell(
            rx.text(label, font_size="13px", font_weight="700", color="#0A1F2E", font_family="'Outfit', sans-serif"),
            background="#F8FAFC",
            width="35%",
        ),
        rx.table.cell(
            rx.text(val, font_size="13px", color="#334155", font_family="'IBM Plex Mono', monospace"),
            width="65%",
        ),
    )


def user_modal() -> rx.Component:
    """
    User Login, Registration, and Profile Management Modal.
    Communicates with backend FastAPI endpoints and SQLite database tables.
    """
    return rx.dialog.root(
        rx.dialog.content(
            # Modal Header Bar
            rx.hstack(
                rx.hstack(
                    rx.icon("user-check", size=22, color="#1B6E5B"),
                    rx.vstack(
                        rx.dialog.title("User Profile & Authentication Portal", font_size="16px", font_weight="700", color="#0A1F2E", font_family="'Space Grotesk', sans-serif", margin_bottom="0"),
                        rx.dialog.description("SQLite Database Table Sync via FastAPI Service", font_size="11px", color="#5A6E72", font_family="'IBM Plex Mono', monospace"),
                        spacing="0",
                    ),
                    spacing="2",
                    align="center",
                ),
                rx.dialog.close(
                    rx.icon("x", size=18, color="#5A6E72", cursor="pointer", on_click=State.toggle_login_modal),  # type: ignore
                ),
                justify="between",
                align="center",
                margin_bottom="16px",
            ),
            
            # Modal Navigation Tabs
            rx.hstack(
                rx.button(
                    "Log In",
                    size="2",
                    background=rx.cond(State.login_tab == "login", "#1B6E5B", "#E2E8F0"),
                    color=rx.cond(State.login_tab == "login", "#FFFFFF", "#0D1B1E"),
                    font_weight="600",
                    on_click=State.set_login_tab("login"),  # type: ignore
                    cursor="pointer",
                    border_radius="6px",
                ),
                rx.button(
                    "Register Profile",
                    size="2",
                    background=rx.cond(State.login_tab == "register", "#1B6E5B", "#E2E8F0"),
                    color=rx.cond(State.login_tab == "register", "#FFFFFF", "#0D1B1E"),
                    font_weight="600",
                    on_click=State.set_login_tab("register"),  # type: ignore
                    cursor="pointer",
                    border_radius="6px",
                ),
                rx.cond(
                    State.is_logged_in,
                    rx.button(
                        "My Profile Table",
                        size="2",
                        background=rx.cond(State.login_tab == "profile", "#1B6E5B", "#E2E8F0"),
                        color=rx.cond(State.login_tab == "profile", "#FFFFFF", "#0D1B1E"),
                        font_weight="600",
                        on_click=State.set_login_tab("profile"),  # type: ignore
                        cursor="pointer",
                        border_radius="6px",
                    ),
                ),
                spacing="2",
                margin_bottom="20px",
            ),
            
            # Error and Success Feedback Banners
            rx.cond(
                State.auth_error != "",
                rx.box(
                    rx.hstack(
                        rx.icon("circle-alert", size=16, color="#C4432E"),
                        rx.text(State.auth_error, font_size="13px", color="#C4432E", font_weight="600"),
                        spacing="2",
                        align="center",
                    ),
                    padding="10px 14px",
                    background="rgba(196, 67, 46, 0.1)",
                    border="1px solid rgba(196, 67, 46, 0.3)",
                    border_radius="6px",
                    margin_bottom="16px",
                ),
            ),
            rx.cond(
                State.auth_success != "",
                rx.box(
                    rx.hstack(
                        rx.icon("circle-check", size=16, color="#10B981"),
                        rx.text(State.auth_success, font_size="13px", color="#10B981", font_weight="600"),
                        spacing="2",
                        align="center",
                    ),
                    padding="10px 14px",
                    background="rgba(16, 185, 129, 0.1)",
                    border="1px solid rgba(16, 185, 129, 0.3)",
                    border_radius="6px",
                    margin_bottom="16px",
                ),
            ),
            
            # Tab 1: Log In Form
            rx.cond(
                State.login_tab == "login",
                rx.vstack(
                    rx.text("Username or Registered Email", font_size="13px", font_weight="600", color="#0A1F2E"),
                    rx.input(
                        placeholder="Enter username or email...",
                        value=State.form_username,
                        on_change=State.set_form_username,  # type: ignore
                        width="100%",
                        padding="10px",
                    ),
                    rx.text("Password", font_size="13px", font_weight="600", color="#0A1F2E"),
                    rx.input(
                        type="password",
                        placeholder="Enter password...",
                        value=State.form_password,
                        on_change=State.set_form_password,  # type: ignore
                        width="100%",
                        padding="10px",
                    ),
                    rx.button(
                        "Log In & Verify Session",
                        background="#1B6E5B",
                        color="#FFFFFF",
                        font_weight="700",
                        width="100%",
                        margin_top="12px",
                        on_click=State.handle_user_login,  # type: ignore
                        cursor="pointer",
                        _hover={"background": "#145C46"},
                    ),
                    spacing="3",
                    align="start",
                    width="100%",
                ),
            ),
            
            # Tab 2: Register Profile Form
            rx.cond(
                State.login_tab == "register",
                rx.vstack(
                    rx.hstack(
                        rx.vstack(
                            rx.text("Full Name *", font_size="12px", font_weight="600", color="#0A1F2E"),
                            rx.input(placeholder="e.g. Rahul Sharma", value=State.form_full_name, on_change=State.set_form_full_name, width="100%"),  # type: ignore
                            width="50%",
                        ),
                        rx.vstack(
                            rx.text("Username *", font_size="12px", font_weight="600", color="#0A1F2E"),
                            rx.input(placeholder="e.g. rahul_sharma", value=State.form_username, on_change=State.set_form_username, width="100%"),  # type: ignore
                            width="50%",
                        ),
                        width="100%",
                        spacing="3",
                    ),
                    rx.hstack(
                        rx.vstack(
                            rx.text("Email Address *", font_size="12px", font_weight="600", color="#0A1F2E"),
                            rx.input(placeholder="rahul@example.com", value=State.form_email, on_change=State.set_form_email, width="100%"),  # type: ignore
                            width="50%",
                        ),
                        rx.vstack(
                            rx.text("Password *", font_size="12px", font_weight="600", color="#0A1F2E"),
                            rx.input(type="password", placeholder="Secret password", value=State.form_password, on_change=State.set_form_password, width="100%"),  # type: ignore
                            width="50%",
                        ),
                        width="100%",
                        spacing="3",
                    ),
                    rx.hstack(
                        rx.vstack(
                            rx.text("Mobile Number *", font_size="12px", font_weight="600", color="#0A1F2E"),
                            rx.input(placeholder="+91 9876543210", value=State.form_mobile, on_change=State.set_form_mobile, width="100%"),  # type: ignore
                            width="50%",
                        ),
                        rx.vstack(
                            rx.text("Age", font_size="12px", font_weight="600", color="#0A1F2E"),
                            rx.input(placeholder="25", value=State.form_age, on_change=State.set_form_age, width="100%"),  # type: ignore
                            width="50%",
                        ),
                        width="100%",
                        spacing="3",
                    ),
                    rx.text("State / UT Address Details", font_size="12px", font_weight="600", color="#0A1F2E"),
                    rx.input(
                        placeholder="e.g. New Delhi, Delhi",
                        value=State.form_address,
                        on_change=State.set_form_address,  # type: ignore
                        width="100%",
                    ),
                    rx.button(
                        "Save Profile to Database Tables",
                        background="#1B6E5B",
                        color="#FFFFFF",
                        font_weight="700",
                        width="100%",
                        margin_top="12px",
                        on_click=State.handle_user_register,  # type: ignore
                        cursor="pointer",
                        _hover={"background": "#145C46"},
                    ),
                    spacing="3",
                    align="start",
                    width="100%",
                ),
            ),
            
            # Tab 3: My Profile Table View
            rx.cond(
                State.login_tab == "profile",
                rx.vstack(
                    rx.heading("Stored User Profile Details (SQLite Table)", font_size="14px", font_weight="700", color="#0A1F2E", font_family="'Space Grotesk', sans-serif"),
                    rx.table.root(
                        rx.table.body(
                            profile_table_row("User ID", State.user_profile["user_id"].to(str)),  # type: ignore
                            profile_table_row("Username", State.user_profile["username"].to(str)),  # type: ignore
                            profile_table_row("Full Name", State.user_profile["full_name"].to(str)),  # type: ignore
                            profile_table_row("Email Address", State.user_profile["email"].to(str)),  # type: ignore
                            profile_table_row("Mobile Number", State.user_profile["mobile_number"].to(str)),  # type: ignore
                            profile_table_row("Age", State.user_profile["age"].to(str)),  # type: ignore
                            profile_table_row("Address / State", State.user_profile["address"].to(str)),  # type: ignore
                        ),
                        variant="surface",
                        width="100%",
                        margin_y="12px",
                    ),
                    rx.button(
                        "Log Out Session",
                        color_scheme="red",
                        variant="soft",
                        width="100%",
                        on_click=State.handle_user_logout,  # type: ignore
                        cursor="pointer",
                    ),
                    spacing="3",
                    align="start",
                    width="100%",
                ),
            ),
            padding="24px",
            max_width="540px",
            border_radius="12px",
            background="#FFFFFF",
        ),
        open=State.login_modal_open,
    )
