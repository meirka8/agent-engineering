import json

with open("./naming_scheme_generator/themes/default_theme.json") as f:
    default_theme = json.load(f)

with open("./naming_scheme_generator/themes/custom_theme_example.json") as f:
    custom_theme_example = json.load(f)
