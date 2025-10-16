import random
import enum

class Role(enum.Enum):
    MARKSMAN = "marksman"
    WARRIOR = "warrior"
    SUPPORT = "support"
    MAGE = "mage"
    ASSASSIN = "assassin"

class PlayerReportCard:
    version = 1

    def __init__(self, username, role):
        if not isinstance(role, Role):
            raise ValueError(f"role must be one of {[[r.value for r in Role]]}")

        self.username = username
        self.role = role
        self.kills = 0
        self.assists = 0
        self.deaths = 0

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
        return f"{self.username} | KDA: {self.kills}-{self.deaths}-{self.assists}"