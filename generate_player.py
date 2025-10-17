from generate_username import generate_username
from player import Player
import random

def generate_player(role):
    age = random.randint(15,30)
    username = generate_username()
    real_name = "X"
    gender = "X"
    attack = random.randint(-5, 5)
    defense = random.randint(-5, 5)
    return Player(username, real_name, age, gender, role, attack, defense)

