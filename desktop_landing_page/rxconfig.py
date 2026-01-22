import reflex as rx

config = rx.Config(
    app_name="desktop_landing_page",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)