import random
from role import Role
from player import Player

class PlayerLatestMatchStats:
    def __init__(self, player: Player):
        self.player = player
        self.role = self.player.current_role
        self.cheated = False
        self.kills = 0
        self.assists = 0
        self.deaths = 0
        self.runes_taken = 0
        self.neutrals_killed = 0

        self.igl_modifier = 0
        if self.player.team.igl:
            if self.player.team.igl.leadership >= 0:
                self.igl_modifier = random.randint(0, self.player.team.igl.leadership)
            else:
                self.igl_modifier = random.randint(self.player.team.igl.leadership, 0)

        match self.role:
            case Role.MARKSMAN:
                self.kills = max(0, random.randint(0, 25 + self.player.attack + self.igl_modifier))
                self.deaths = max(0, random.randint(0, 20 - self.player.defense - self.igl_modifier))
                self.assists = max(0, random.randint(0, 15 + self.player.attack + self.igl_modifier))
            case Role.WARRIOR:
                self.kills = max(0, random.randint(0, 15 + self.player.attack + self.igl_modifier))
                self.deaths = max(0, random.randint(0, 15 - self.player.defense - self.igl_modifier))
                self.assists = max(0, random.randint(0, 25 + self.player.attack + self.igl_modifier))
            case Role.SUPPORT:
                self.kills = max(0, random.randint(0, 10 + self.player.attack + self.igl_modifier))
                self.deaths = max(0, random.randint(0, 25 - self.player.defense - self.igl_modifier))
                self.assists = max(0, random.randint(0, 20 + self.player.attack + self.igl_modifier))
            case Role.MAGE:
                self.kills = max(0, random.randint(0, 20 + self.player.attack + self.igl_modifier))
                self.deaths = max(0, random.randint(0, 20 - self.player.defense - self.igl_modifier))
                self.assists = max(0, random.randint(0, 25 + self.player.attack + self.igl_modifier))
            case Role.ASSASSIN:
                self.kills = max(0, random.randint(0, 25 + self.player.attack + self.igl_modifier))
                self.deaths = max(0, random.randint(0, 25 - self.player.defense - self.igl_modifier))
                self.assists = max(0, random.randint(0, 10 + self.player.attack + self.igl_modifier))

    def string(self):
        return f"{self.player.username} | {self.role.value} | KDA: {self.kills}-{self.deaths}-{self.assists} | Runes taken: {self.runes_taken} | Neutrals killed: {self.neutrals_killed}"
    
    def kda(self):
        return self.kills + self.assists - self.deaths
    
    def make_cheater(self):
        self.kills = self.kills + round(self.kills / 2)
        self.assists = self.assists + round(self.kills / 2)
        self.runes_taken = self.runes_taken + random.randint(2, 30)
        self.runes_taken = self.runes_taken + random.randint(5, 35)
        self.cheated = True