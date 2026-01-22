import reflex as rx

# Colores

PRI_BLUE = "#2091F9"
WHITE = "#FFFFFF"
DARK_NAVY = "#252B42"
TEXT_DARK = "#252B42"
TEXT_SECONDARY = "#374754"
INPUT_BG = "#F5F5F5"
INPUT_BORDER = "#E8E8E8"
TEXT_BLACK = "#18171D"
TEXT_DARK_NAVY = "#252B42" 
TEXT_SLATE_GREY = "#374754" 
INPUT_BLACK = "#18171D"
CARD_BG = "#FFFFFF"
CARD_BORDER = "#DDDDDD"
NAVY_TITLE = "#252B42"

# Estilos de texto

header_style = {
    "font_family": "Inter",
    "font_weight": "700",
    "font_size": "74px",
    "line_height": "84px",
    "text_align": "center",
    "letter_spacing": "0.2px",
    "color": WHITE,
}

sub_header_style = {
    "font_family": "Inter",
    "font_weight": "400",
    "font_size": "28px",
    "line_height": "40px",
    "text_align": "center",
    "letter_spacing": "0.2px",
    "color": WHITE,
}

nav_link_style = {
    "color": WHITE,
    "font_size": "15px",
    "font_weight": "400",
    "_hover": {"cursor": "pointer", "opacity": 0.7}
}

features_h2_style = {
    "font_family": "Inter",
    "font_weight": "400",
    "font_size": "48px",
    "line_height": "55px",
    "text_align": "center",
    "letter_spacing": "0.2px",
    "color": "#252B42",
}

features_h4_style = {
    "font_family": "Inter",
    "font_weight": "400",
    "font_size": "28px",
    "line_height": "40px",
    "text_align": "center",
    "letter_spacing": "0.2px",
    "color": "#374754",
    "max_width": "532px",
}

feature_title_style = {
    "font_family": "Inter",
    "font_weight": "700",
    "font_size": "20px",
    "color": TEXT_DARK,
    "text_align": "center",
}

feature_desc_style = {
    "font_family": "Inter",
    "font_weight": "400",
    "font_size": "16px",
    "line_height": "24px",
    "color": TEXT_SECONDARY,
    "text_align": "center",
}

contact_h2_style = {
    "font_family": "Inter",
    "font_weight": "400",
    "font_size": "48px",
    "color": "#252B42",
    "text_align": "center",
}

form_card_style = {
    "background": CARD_BG,
    "border": f"1px solid {CARD_BORDER}",
    "box_shadow": "0px 13px 19px rgba(0, 0, 0, 0.07)",
    "border_radius": "20px",
    "padding": "52px 50px",
    "width": "453px",
    "height": "669px",
    "display": "flex",
    "flex_direction": "column",
}

input_style = {
    "background_color": INPUT_BG,
    "border": f"1px solid {INPUT_BORDER}",
    "border_radius": "39px",
    "height": "54px",
    "width": "353px",
    "padding": "19px 20px",
    "color": TEXT_BLACK,
    "font_family": "Roboto, sans-serif",
    "font_size": "15px",
    "font_weight": "400",
    "letter_spacing": "0.1px",
    "_placeholder": {
        "color": TEXT_BLACK,
        "opacity": "1",
    },
}

text_area_style = {
    **input_style,
    "height": "193px",
    "border_radius": "10px",
}

sidebar_title_style = {
    "font_family": "Inter",
    "font_weight": "700",
    "font_size": "20px",
    "line_height": "28px",
    "letter_spacing": "0.1px",
    "color": TEXT_DARK_NAVY,
}

contact_label_style = {
    "font_family": "Inter",
    "font_weight": "400",
    "font_size": "16px",
    "line_height": "23px",
    "letter_spacing": "0.1px",
    "color": TEXT_SLATE_GREY,
    "text_align": "center",
}