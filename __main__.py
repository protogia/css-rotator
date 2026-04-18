import random
import dotenv
import os
dotenv.load_dotenv()

themes = [
    {
        "name": "blue", 
        "bg": "#15151d", 
        "h1": "#34a1bd", 
        "h2": "#a09f93", 
        "text": "#f2f0ec", 
        "accent": "#ff1e00", 
        "code-bg": "#0d1117"
    },
    {
        "name": "red",
        "bg": "#4A2626",
        "h1": "#D93A3A", 
        "h2": "#a09f93", 
        "text": "#FFFFFF", 
        "accent": "#2BFF88", 
        "code-bg": "#0A0808"
    },
    {
        "name": "violet",
        "bg": "#1a162d",
        "h1": "#B96EF4",
        "h2": "#9A9AA0",
        "text": "#FFFFFF",
        "accent": "#00FFC2",
        "code-bg": "#09080d"
    },
    {
        "name": "yellow",
        "bg": "#1e1a00",
        "h1": "#FFD54F",
        "h2": "#A09F93",
        "text": "#FFFFFF",
        "accent": "#7B61FF",
        "code-bg": "#0f0d00"
    },
    {
        "name": "green",
        "bg": "#0d1a12",
        "h1": "#38C075",
        "h2": "#8C9A84",
        "text": "#FFFFFF",
        "accent": "#FF4DCC",
        "code-bg": "#050a07"
    },
    {
        "name": "orange",
        "bg": "#241400",
        "h1": "#FFB84D",
        "h2": "#A09F93",
        "text": "#FFFFFF",
        "accent": "#00E5FF",
        "code-bg": "#120a00"
    },
    {
        "name": "grey",
        "bg": "#121212",
        "h1": "#E0E0E0",
        "h2": "#A09F93",
        "text": "#FFFFFF",
        "accent": "#FF3E3E",
        "code-bg": "#000000"
    },
    {
        "name": "white",
        "bg": "#FFFFFF",
        "h1": "#2C3E50",
        "h2": "#7F8C8D",
        "text": "#34495E",
        "accent": "#6C5CE7",
        "code-bg": "#EDF2F7"     
    }
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
