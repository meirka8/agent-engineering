import json
import random
from typing import Dict, List
from .themes import default_theme

def generate_name(theme) -> str:
    letter = random.choice(list(theme.keys()))
    adjective = random.choice(theme[letter]['adjectives'])
    noun = random.choice(theme[letter]['nouns'])
    return f"{adjective}_{noun}"

def load_custom_theme(file_path: str):
    with open(file_path, "r") as file:
        custom_theme = json.load(file)
    return custom_theme

def generate_name_with_theme(theme: str = "default") -> str:
    if theme == "default":
        theme = default_theme
    else:
        custom_theme = load_custom_theme(theme)

    return generate_name(theme)