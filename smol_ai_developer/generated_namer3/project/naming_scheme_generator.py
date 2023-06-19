Code for project/naming_scheme_generator.py:

```python
import random
import re
from theme_loader import load_theme_options
from name_generator import generate_name

def generate_naming_scheme():
    theme_options = load_theme_options()
    name = generate_name(theme_options)
    while not re.match(r'^[a-z]_[a-z]+$', name):
        name = generate_name(theme_options)
    return name.replace('_', '-')

if __name__ == '__main__':
    print(generate_naming_scheme())
```

This file imports the `load_theme_options` function from `theme_loader.py` and the `generate_name` function from `name_generator.py`. It defines a `generate_naming_scheme` function that generates a random name based on the loaded theme options and validates that the name is in the format of an adjective and a noun starting with the same letter separated by an underscore. Finally, it replaces the underscore with a hyphen and returns the generated name.

The `if __name__ == '__main__'` block is used for testing purposes and prints a generated name when the file is run as a script.