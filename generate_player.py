from generate_username import generate_username
from generate_real_name import generate_real_name
from player import Player
import random

def generate_player(role):
    age = random.randint(15,30)
    gender = "X"
    chance = random.randint(1, 8)
    if chance < 2:
        gender = "enby"
    elif chance < 5:
        gender = "afab"
    else:
        gender = "amab"
    username = generate_username()
    real_name = generate_real_name(gender)
    attack = random.randint(-5, 5)
    defense = random.randint(-5, 5)
    return Player(username, real_name, age, gender, role, attack, defense)

