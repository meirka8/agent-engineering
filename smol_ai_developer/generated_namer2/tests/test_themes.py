import json
import os
import unittest
from naming_scheme_generator import generator, themes

class TestThemes(unittest.TestCase):

    def test_load_custom_theme(self):
        custom_theme_path = "naming_scheme_generator/themes/custom_theme_example.json"
        custom_theme = themes.load_custom_theme(custom_theme_path)
        self.assertIsInstance(custom_theme, themes.Theme)

        with open(custom_theme_path, "r") as f:
            custom_theme_data = json.load(f)

        for letter, theme_data in custom_theme_data.items():
            self.assertEqual(custom_theme.adjectives[letter], theme_data["adjectives"])
            self.assertEqual(custom_theme.nouns[letter], theme_data["nouns"])

    def test_generate_name_default_theme(self):
        default_theme = themes.default_theme
        generated_name = generator.generate_name(default_theme.adjectives, default_theme.nouns)
        self.assertIsInstance(generated_name, str)
        self.assertEqual(len(generated_name.split(" ")), 2)

        adjective, noun = generated_name.split(" ")
        self.assertEqual(adjective[0], noun[0])

    def test_generate_name_custom_theme(self):
        custom_theme_path = "naming_scheme_generator/themes/custom_theme_example.json"
        custom_theme = themes.load_custom_theme(custom_theme_path)
        generated_name = generator.generate_name(custom_theme.adjectives, custom_theme.nouns)
        self.assertIsInstance(generated_name, str)
        self.assertEqual(len(generated_name.split(" ")), 2)

        adjective, noun = generated_name.split(" ")
        self.assertEqual(adjective[0], noun[0])

if __name__ == "__main__":
    unittest.main()