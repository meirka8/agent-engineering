import random
from adjectives import adjectives
from nouns import nouns

def get_random_element(arr):
    return random.choice(arr)

def generate_random_name():
    random_letter = chr(97 + random.randint(0, 25))
    adjective = get_random_element(adjectives[random_letter])
    noun = get_random_element(nouns[random_letter])
    return f"{adjective}-{noun}"

if __name__ == "__main__":
    print(generate_random_name())