import json
import os
import unittest
from naming_scheme_generator import generator, themes

class TestThemes(unittest.TestCase):

    def test_load_custom_theme(self):
        custom_theme_path = "naming_scheme_generator/themes/custom_theme_example.json"
        custom_theme = generator.load_custom_theme(custom_theme_path)
        self.assertIsInstance(custom_theme, dict)

        with open(custom_theme_path, "r") as f:
            custom_theme_data = json.load(f)

        for letter, theme_data in custom_theme_data.items():
            self.assertEqual(custom_theme[letter]['adjectives'], theme_data["adjectives"])
            self.assertEqual(custom_theme[letter]['nouns'], theme_data["nouns"])

    def test_generate_name_default_theme(self):
        default_theme = themes.default_theme
        generated_name = generator.generate_name(default_theme)
        self.assertIsInstance(generated_name, str)
        self.assertEqual(len(generated_name.split("_")), 2)

        adjective, noun = generated_name.split("_")
        self.assertEqual(adjective[0], noun[0])

    def test_generate_name_custom_theme(self):
        custom_theme_path = "naming_scheme_generator/themes/custom_theme_example.json"
        custom_theme = generator.load_custom_theme(custom_theme_path)
        generated_name = generator.generate_name(custom_theme)
        print(generated_name)
        self.assertIsInstance(generated_name, str)
        self.assertEqual(len(generated_name.split("_")), 2)

        adjective, noun = generated_name.split("_")
        self.assertEqual(adjective[0], noun[0])

if __name__ == "__main__":
    unittest.main()