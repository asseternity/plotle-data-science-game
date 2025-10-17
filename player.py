class Player:
    def __init__(self, username, real_name, age, gender, current_role, attack, defense):
        self.username = username
        self.real_name = real_name
        self.age = age
        self.gender = gender
        self.current_role = current_role
        self.attack = attack
        self.defense = defense
        self.latest_match = None
        self.match_history = []