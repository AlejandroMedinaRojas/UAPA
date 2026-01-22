import reflex as rx
from .styles import *

def navbar():
    return rx.box(
        rx.hstack(
            # Links
            rx.hstack(
                rx.link("Home", href="#", style=nav_link_style),
                rx.link("Product", href="#", style=nav_link_style),
                rx.link("Pricing", href="#", style=nav_link_style),
                rx.link("About", href="#", style=nav_link_style),
                rx.link("Contact", href="#", style=nav_link_style),
                spacing="5",
            ),
            rx.spacer(),
            
            # Logo
            rx.image(src="/logo.png", height="40px"),
            rx.spacer(),
            
            # Redes sociales
            rx.hstack(
                rx.icon(tag="twitter", color=WHITE),
                rx.icon(tag="facebook", color=WHITE),
                rx.icon(tag="linkedin", color=WHITE),
                spacing="4",
            ),
            width="100%",
            max_width="1200px",
            align_items="center",
        ),
        width="100%",
        padding="2em 4em",
        position="absolute",
        top="0",
        z_index="10",
        display="flex",
        justify_content="center",
    )

def hero():
    return rx.box(
        rx.vstack(
            rx.heading("The best products start with Figma", style=header_style, max_width="672px"),
            rx.text(
                "Most calendars are designed for teams. Slate is designed for freelancers",
                style=sub_header_style,
                max_width="766px",
                margin_top="20px",
            ),
            rx.button(
                "Try For Free",
                background_color=PRI_BLUE,
                color=WHITE,
                border_radius="35px",
                padding="1.8em 3.5em",
                margin_top="40px",
                font_weight="bold",
                _hover={"transform": "scale(1.05)"},
            ),
            spacing="5",
            padding_top="180px",
            padding_bottom="150px",
            align_items="center",
        ),
        width="100%",
        background_image="url('/hero_bg.jpg')",
        background_size="cover",
        background_position="center",
        clip_path="polygon(0 0, 100% 0, 100% 88%, 50% 100%, 0 88%)",
    )

def feature_item(icon_name, title, description):
    return rx.vstack(
        rx.image(
            src=f"/{icon_name}.svg", 
            width="40px", 
            height="auto"
        ),
        rx.text(title, style=feature_title_style, margin_top="10px"),
        rx.text(description, style=feature_desc_style),
        align_items="center",
        spacing="3",
        width="100%",
        max_width="300px",
    )

def features_section():
    return rx.box(
        rx.vstack(
            rx.vstack(
                rx.heading("Features", style=features_h2_style),
                rx.text(
                    "Most calendars are designed for teams. Slate is designed for freelancers",
                    style=features_h4_style,
                ),
                spacing="2",
                align_items="center",
                width="100%",
                padding_y="80px",
            ),
            
            # Iconos
            rx.hstack(
                feature_item(
                    "icon_opentype",
                    "OpenType features Variable fonts", 
                    "Slate helps you see how many more days you need to work to reach your financial goal."
                ),
                feature_item(
                    "icon_data",
                    "Design with real data", 
                    "Slate helps you see how many more days you need to work to reach your financial goal."
                ),
                feature_item(
                    "icon_action",
                    "Fastest way to take action", 
                    "Slate helps you see how many more days you need to work to reach your financial goal."
                ),
                width="100%",
                max_width="1200px",
                justify="between",
                spacing="8",
            ),

            # Video
            rx.box(
                rx.image(
                    src="/video_placeholder.png",
                    border_radius="20px",
                    box_shadow="0px 20px 40px rgba(0,0,0,0.1)",
                    width="100%",
                ),
                position="relative",
                padding_y="100px",
                max_width="1000px",
            ),
            width="100%",
            align_items="center",
        ),
        width="100%",
        background_color=WHITE,
        display="flex",
        justify_content="center",
    )

def contact_section():
    return rx.box(
        rx.vstack(
            # Encabezado
            rx.vstack(
                rx.heading("Contact Us", style=contact_h2_style),
                rx.text(
                    "Most calendars are designed for teams. Slate is designed for freelancers",
                    style=features_h4_style,
                ),
                spacing="2",
                padding_y="60px",
                align_items="center",
                width="100%",
            ),

            rx.hstack(
                # Carta de input
                rx.vstack(
                    rx.text("Contact Us", style=sidebar_title_style, align_self="center"),
                    rx.input(placeholder="Your Name", style=input_style),
                    rx.input(placeholder="Your Email", style=input_style),
                    rx.text_area(placeholder="Your Message", style=text_area_style),
                    rx.button(
                        "Send", 
                        bg="#2091F9", 
                        color="#FFFFFF", 
                        border_radius="35px",
                        width="145px", 
                        height="56px",
                        font_size="20px",
                        font_family="Inter",
                        _hover={"opacity": 0.8}
                    ),
                    style=form_card_style,
                    spacing="7",
                    align_items="flex-start",
                ),

                # Mapa y contacto
                rx.vstack(
                    # Iconos
                    rx.hstack(
                        rx.vstack(rx.icon(tag="map-pin", color=PRI_BLUE), rx.text("6386 Spring St...", style=contact_label_style)),
                        rx.vstack(rx.icon(tag="phone", color=PRI_BLUE), rx.text("(843) 555-0130", style=contact_label_style)),
                        rx.vstack(rx.icon(tag="mail", color=PRI_BLUE), rx.text("willie@example.com", style=contact_label_style)),
                        spacing="8",
                    ),
                    # Mapa
                    rx.image(
                        src="/map.png",
                        width="100%",
                        height="auto",
                        margin_top="40px",
                        border_radius="10px",
                    ),
                    # Redes sociales
                    rx.hstack(
                        rx.icon(tag="twitter", color=PRI_BLUE),
                        rx.icon(tag="facebook", color=PRI_BLUE),
                        rx.icon(tag="linkedin", color=PRI_BLUE),
                        spacing="4",
                        margin_top="30px",
                    ),
                    width="100%",
                    max_width="500px",
                    align_items="center",
                    padding_left="40px",
                ),
                spacing="9",
                width="100%",
                max_width="1200px",
                justify="center",
                align_items="start",
            ),
            padding_y="100px",
            width="100%",
            align_items="center",
        ),
        width="100%",
        display="flex",
        justify_content="center",
    )

def footer():
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text("Pages", font_weight="bold", color="white", margin_bottom="10px"),
                rx.link("Home", color="white", font_size="14px"),
                rx.link("Product", color="white", font_size="14px"),
                rx.link("Pricing", color="white", font_size="14px"),
                rx.link("About", color="white", font_size="14px"),
                rx.link("Contact", color="white", font_size="14px"),
                align_items="start",
            ),
            rx.vstack(
                rx.text("Tomothy", font_weight="bold", color="white", margin_bottom="10px"),
                rx.text("Eleanor Edwards", color="white", font_size="14px"),
                rx.text("Ted Robertson", color="white", font_size="14px"),
                rx.text("Annette Russell", color="white", font_size="14px"),
                rx.text("Jennie Mckinney", color="white", font_size="14px"),
                rx.text("Gloria Richards", color="white", font_size="14px"),
                align_items="start",
            ),
            rx.vstack(
                rx.text("Jane Black", font_weight="bold", color="white", margin_bottom="10px"),
                rx.text("Philip Jones", color="white", font_size="14px"),
                rx.text("Product", color="white", font_size="14px"),
                rx.text("Collen Russell", color="white", font_size="14px"),
                rx.text("Marvin Hawkins", color="white", font_size="14px"),
                rx.text("Bruce Simmmons", color="white", font_size="14px"),
                align_items="start",
            ),
            rx.vstack(
                rx.hstack(rx.icon(tag="map-pin", color="white"), rx.text("7480 Mockingbird Hill undefined", color="white", font_size="14px")),
                rx.hstack(rx.icon(tag="phone", color="white"), rx.text("(239) 555-0108", color="white", font_size="14px")),
                rx.hstack(
                    rx.icon(tag="twitter", color="white"),
                    rx.icon(tag="facebook", color="white"),
                    rx.icon(tag="linkedin", color="white"),
                    spacing="4",
                    margin_top="20px"
                ),
                align_items="start",
            ),
            justify="between",
            width="100%",
            max_width="1200px",
            padding="100px 20px",
        ),
        background_color="#252B42",
        width="100%",
        display="flex",
        justify_content="center",
    )