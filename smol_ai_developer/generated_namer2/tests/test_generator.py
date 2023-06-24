import unittest
from naming_scheme_generator.generator import generate_name, load_custom_theme
from naming_scheme_generator.themes import default_theme

class TestGenerator(unittest.TestCase):

    def test_generate_name_default_theme(self):
        name = generate_name(default_theme)
        self.assertIsNotNone(name)
        self.assertTrue(isinstance(name, str))
        self.assertEqual(len(name.split("_")), 2)
        self.assertEqual(name.split("_")[0][0], name.split("_")[1][0])

    def test_generate_name_custom_theme(self):
        custom_theme = load_custom_theme("naming_scheme_generator/themes/custom_theme_example.json")
        name = generate_name(custom_theme)
        self.assertIsNotNone(name)
        self.assertTrue(isinstance(name, str))
        self.assertEqual(len(name.split("_")), 2)
        self.assertEqual(name.split("_")[0][0], name.split("_")[1][0])

    def test_load_custom_theme(self):
        custom_theme = load_custom_theme("naming_scheme_generator/themes/custom_theme_example.json")
        self.assertIsNotNone(custom_theme)
        self.assertTrue(hasattr(custom_theme, "adjectives"))
        self.assertTrue(hasattr(custom_theme, "nouns"))

if __name__ == '__main__':
    unittest.main()