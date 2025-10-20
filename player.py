class Player:
    def __init__(self, username, real_name, age, gender, attack, defense, leadership):
        self.username = username
        self.real_name = real_name
        self.age = age
        self.gender = gender
        self.attack = attack
        self.defense = defense
        self.leadership = leadership

        self.current_role = None
        self.team = None
        self.latest_match = None
        self.match_history = []

    def get_role_name(self):
        return self.current_role.value if self.current_role else "Unassigned"

    def set_role_if_unoccupied(self, role):
        role_taken = False
        for teammate in self.team.roster:
            if teammate.current_role == role:
                role_taken = True
        if role_taken == False:
            self.current_role = role
            return True
        else:
            return False