import reflex as rx
from .components import navbar, hero, features_section, contact_section, footer

def index() -> rx.Component:
    return rx.box(
        navbar(),
        hero(),
        features_section(),
        contact_section(),
        footer(),

        width="100%",
        background_color="#FFFFFF",
        overflow_x="hidden",
    )

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap",
    ],
)
app.add_page(index)