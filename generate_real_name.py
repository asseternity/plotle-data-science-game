import random
import json

with open('data/real_names.json') as f:
    data = json.load(f)

def generate_real_name(gender):
    firstName = ""
    surname = data['surnames'][random.randint(0, len(data['surnames']) - 1)]

    if gender == "amab":
        firstName = data['amab_names'][random.randint(0, len(data['amab_names']) - 1)]
    elif gender == "afab":
        firstName = data['afab_names'][random.randint(0, len(data['afab_names']) - 1)]
    else:
        firstName = data['enby_names'][random.randint(0, len(data['enby_names']) - 1)]

    return f"{firstName} {surname}"