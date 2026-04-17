import random
import dotenv
import os
dotenv.load_dotenv()

themes = [
    {"name": "blue", "bg": "#15151d", "h1": "#34a1bd", "h2": "#a09f93", "text": "#f2f0ec", "accent": "#ff1e00", "code-bg": "#0d1117"},
    {"name": "red", "bg": "#4A2626", "h1": "#D93A3A", "h2": "#a09f93", "text": "#FFFFFF", "accent": "#F2C94C", "code-bg": "#0A0808"},
    {"name": "violet", "bg": "#32285A", "h1": "#B96EF4", "h2": "#9A9AA0", "text": "#FFFFFF", "accent": "#F2C94C", "code-bg": "#09080D"},
    {"name": "yellow", "bg": "#5C4A00", "h1": "#FFD54F", "h2": "#A09F93", "text": "#FFFFFF", "accent": "#4A90E2", "code-bg": "#3F3A2E"},
    {"name": "green", "bg": "#1F4B31", "h1": "#38C075", "h2": "#8C9A84", "text": "#FFFFFF", "accent": "#FF7F27", "code-bg": "#0A0F0A"},
    {"name": "orange", "bg": "#7A4500", "h1": "#FFB84D", "h2": "#A09F93", "text": "#FFFFFF", "accent": "#B96EF4", "code-bg": "#3B2000"},
    {"name": "grey", "bg": "#393939", "h1": "#E0E0E0", "h2": "#A09F93", "text": "#FFFFFF", "accent": "#FF7F27", "code-bg": "#202020"}
]

selected = random.choice(themes)

# generate css
css_content = f"""/* Theme: {selected['name']} - Generated */
:root {{
  --bg: {selected['bg']};
  --h1: {selected['h1']};
  --h2: {selected['h2']};
  --text: {selected['text']};
  --accent: {selected['accent']};
  --code-bg: {selected['code-bg']};
}}
"""

with open(os.getenv("CSS_VAR_PATH"), "w") as f:
    f.write(css_content)

print(f"Theme changed to {selected['name']}.")
