import random
import enum

class Role(enum.Enum):
    MARKSMAN = "Marksman"
    WARRIOR = "Warrior"
    SUPPORT = "Support"
    MAGE = "Mage"
    ASSASSIN = "Assassin"

class PlayerReportCard:
    version = 1

    def __init__(self, username, role: Role):
        self.username = username
        self.role = role
        self.cheater = False
        self.kills = 0
        self.assists = 0
        self.deaths = 0
        self.runes_taken = 0
        self.neutrals_killed = 0

        match role:
            case Role.MARKSMAN:
                self.kills = random.randint(0, 25)
                self.deaths = random.randint(0, 20)
                self.assists = random.randint(0, 15)
            case Role.WARRIOR:                
                self.kills = random.randint(0, 15)
                self.deaths = random.randint(0, 15)
                self.assists = random.randint(0, 20)
            case Role.SUPPORT:                
                self.kills = random.randint(0, 10)
                self.deaths = random.randint(0, 25)
                self.assists = random.randint(0, 20)
            case Role.MAGE:                
                self.kills = random.randint(0, 20)
                self.deaths = random.randint(0, 20)
                self.assists = random.randint(0, 25)
            case Role.ASSASSIN:                
                self.kills = random.randint(0, 25)
                self.deaths = random.randint(0, 25)
                self.assists = random.randint(0, 10)

    def string(self):
        return f"{self.username} | {self.role.value} | KDA: {self.kills}-{self.deaths}-{self.assists} | Runes taken: {self.runes_taken} | Neutrals killed: {self.neutrals_killed}"
    
    def kda(self):
        return self.kills + self.assists - self.deaths
    
    def make_cheater(self):
        self.kills = self.kills + round(self.kills / 2)
        self.assists = self.assists + round(self.kills / 2)
        self.runes_taken = self.runes_taken + random.randint(2, 30)
        self.runes_taken = self.runes_taken + random.randint(5, 35)
        self.cheater = True