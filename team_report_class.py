from player_report_class import PlayerReportCard, Role
from username_generator import generate_username
from team_name_generator import generate_team_name
import random

class TeamReportCard():
    version = 1

    def __init__(self):
        self.name = generate_team_name()
        self.roster = [
            PlayerReportCard(generate_username(), Role.WARRIOR),
            PlayerReportCard(generate_username(), Role.MAGE),
            PlayerReportCard(generate_username(), Role.MARKSMAN),
            PlayerReportCard(generate_username(), Role.ASSASSIN),
            PlayerReportCard(generate_username(), Role.SUPPORT)
            ]
        chance = random.randint(1,100)
        if chance < 50:
            self.roster[random.randint(0, len(self.roster) - 1)].make_cheater()
        if chance < 20:
            chance2 = random.randint(0, len(self.roster) - 1)
            if (self.roster[chance2].cheater):
                chance3 = random.randint(0, len(self.roster) - 1)
                if (not self.roster[chance3].cheater):
                    self.roster[chance3].make_cheater()
            else:
                self.roster[chance2].make_cheater()

    def total_kills(self):
        total_kills = 0
        for player in self.roster:
            total_kills += player.kills
        return total_kills
    
    def total_assists(self):
        total_assists = 0
        for player in self.roster:
            total_assists += player.assists
        return total_assists
    
    def total_deaths(self):
        total_deaths = 0
        for player in self.roster:
            total_deaths += player.deaths
        return total_deaths

    def print_report(self):
        print("---------------------")
        print("TEAM:", self.name)
        for player in self.roster:
            print(player.string())
        