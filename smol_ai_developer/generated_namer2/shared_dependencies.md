the app is: naming scheme generator

the files we have decided to generate are: main.py, themes.py, custom_themes.py, test_naming_scheme_generator.py

Shared dependencies:
1. Function names:
   - generate_name(theme_adjective, theme_noun)
   - load_custom_theme(file_path)
2. Data schemas:
   - Theme (adjectives: List[str], nouns: List[str])
   - CustomTheme (file_path: str, theme: Theme)
3. Exported variables:
   - default_theme (instance of Theme)
4. JSON structure for custom themes:
   - { "A": { "adjectives": ["adjective1", "adjective2"], "nouns": ["noun1", "noun2"] }, "B": {...}, ... }
5. Test function names:
   - test_generate_name_default_theme()
   - test_generate_name_custom_theme()
   - test_load_custom_theme()