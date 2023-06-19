This project is a naming scheme generator.
It has to be subject to the following tech stack:
1. Programming language: wherever possible, but not limited to python
It has to be subject to the following specification:
1. Having an importable and callable method in python that returns a random name
2. Said name has to be a pair of an adjective and a noun starting with the same letter to the likes of docker container naming convention
3. Adjective and noun have to be of specific theme. Default themes should emotional description, e.g. dramatic for adjective and an abstract entity like manifold for noun.
4. Apart from the default themes, theme pair should be customizable by providing a json with list of available options per each letter of the English alphabet. Providing the json can be constrained to a certain folder inside the project structure. Said json should be explicitly read by python's json library to a dictionary and then used throughout other modules of the project
5. it has to have tests in pytest, evaluating extensiveness of fulfilling the above specifications