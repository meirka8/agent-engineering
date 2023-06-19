import random
from typing import Dict, List
from .themes import default_theme

def generate_name(theme_adjective: Dict[str, List[str]], theme_noun: Dict[str, List[str]]) -> str:
    letter = random.choice(list(theme_adjective.keys()))
    adjective = random.choice(theme_adjective[letter])
    noun = random.choice(theme_noun[letter])
    return f"{adjective}_{noun}"

def load_custom_theme(file_path: str) -> Dict[str, List[str]]:
    with open(file_path, "r") as file:
        custom_theme = json.load(file)
    return custom_theme

def generate_name_with_theme(theme: str = "default") -> str:
    if theme == "default":
        theme_adjective = default_theme["adjectives"]
        theme_noun = default_theme["nouns"]
    else:
        custom_theme = load_custom_theme(theme)
        theme_adjective = custom_theme["adjectives"]
        theme_noun = custom_theme["nouns"]

    return generate_name(theme_adjective, theme_noun)