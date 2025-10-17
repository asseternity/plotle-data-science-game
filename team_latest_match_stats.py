import random
from team import Team
from player_latest_match_stats import PlayerLatestMatchStats

class TeamLatestMatchStats():
    def __init__(self, team: Team):
        self.team = team
        self.player_stats = []

        # fill player stats
        for player in self.team.roster:
            player_stats = PlayerLatestMatchStats(player)
            self.player_stats.append(player_stats)
           
    def assign_match_cheaters(self):
        chance = random.randint(1,100)
        if chance < 50:
            self.player_stats[random.randint(0, len(self.player_stats) - 1)].make_cheater()
        if chance < 20:
            chance2 = random.randint(0, len(self.player_stats) - 1)
            if (self.player_stats[chance2].cheated):
                chance3 = random.randint(0, len(self.player_stats) - 1)
                if (not self.player_stats[chance3].cheated):
                    self.player_stats[chance3].make_cheater()
            else:
                self.player_stats[chance2].make_cheater()

    def total_kills(self):
        total_kills = 0
        for player in self.player_stats:
            total_kills += player.kills
        return total_kills
    
    def total_assists(self):
        total_assists = 0
        for player in self.player_stats:
            total_assists += player.assists
        return total_assists
    
    def total_deaths(self):
        total_deaths = 0
        for player in self.player_stats:
            total_deaths += player.deaths
        return total_deaths

    def print_report(self):
        print("---------------------")
        print("TEAM:", self.team.name)
        for player in self.player_stats:
            print(player.string())
        print("Total KDA:", f"{self.total_kills()}-{self.total_deaths()}-{self.total_assists()}")