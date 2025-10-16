import random
import json
with open('team_names.json') as f:
    data = json.load(f)

def generate_team_name():
    firstWord = data['first_words'][random.randint(0, len(data['first_words']) - 1)]
    secondWord = data['second_words'][random.randint(0, len(data['second_words']) - 1)]
    finalName = firstWord + " " + secondWord
    return finalName

