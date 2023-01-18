import json


def load_db():
    with open('questions.json') as file:
        return json.load(file)


db = load_db()
