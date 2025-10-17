from team_report_class import TeamReportCard
import random

class Match():
    def __init__(self, team1report: TeamReportCard, team2report: TeamReportCard):
        self.team1report = team1report
        self.team2report = team2report
        self.winner = None
        self.duration_in_minutes = None

        # adjust team1's death numbers to match the team2's kill numbers
        team1_deaths_too_many = team1report.total_deaths() - team2report.total_kills()
        team1_player_index = 0
        while team1_deaths_too_many != 0:
            if team1_player_index == 4:
                team1_player_index = 0
            else:
                team1_player_index += 1
            if team1_deaths_too_many > 0:
                team1report.roster[team1_player_index].deaths -= 1
                team1_deaths_too_many -= 1
            elif team1_deaths_too_many < 0:
                team1report.roster[team1_player_index].deaths += 1
                team1_deaths_too_many += 1

        # adjust team2's death numbers to match the team1's kill numbers
        team2_deaths_too_many = team2report.total_deaths() - team1report.total_kills()
        team2_player_index = 0
        while team2_deaths_too_many != 0:
            if team2_player_index == 4:
                team2_player_index = 0
            else:
                team2_player_index += 1
            if team2_deaths_too_many > 0:
                team2report.roster[team2_player_index].deaths -= 1
                team2_deaths_too_many -= 1
            elif team2_deaths_too_many < 0:
                team2report.roster[team2_player_index].deaths += 1
                team2_deaths_too_many += 1

        # determine match winner 
        team1KDA = team1report.total_kills() + team1report.total_assists() - team1report.total_deaths()
        team2KDA = team2report.total_kills() + team2report.total_assists() - team2report.total_deaths()
        KDA_difference = team1KDA - team2KDA
        if KDA_difference > 0:
            self.winner = team1report
        else:
            self.winner = team2report

        # determine match duration
        all_actions = team1report.total_kills() + team1report.total_assists() + team1report.total_deaths() + team2report.total_kills() + team2report.total_assists() + team2report.total_deaths()
        self.duration_in_minutes = round(all_actions / 5)

        # determine how many runes have spawned [50% chance to spawn 1 every minute; players will on average grab 90% of them]
        total_runes_spawned = 0
        for minute in range(self.duration_in_minutes):
            chance = random.randint(0, 1)
            if chance == 1:
                total_runes_spawned += 1
        runes_taken_total = int(total_runes_spawned * 0.9)  # 90% grabbed

        # determine how many runes were taken, split by players from both teams
        # first, create a percentage separation split between 10 players that adds up to 100
        # then sort it by desc
        # then assign it between players, sorted by KDA 
        initial_split = [20, 17, 15, 12, 10, 8, 6, 5, 4, 3]
        for i in range(len(initial_split)):
            chance = random.randint(0, 1)
            if chance == 1:
                change = random.randint(1, 5)
                initial_split[i] = initial_split[i] - change
                other_player_index = random.randint(0, len(initial_split) - 1)
                initial_split[other_player_index] = initial_split[other_player_index] + change
        initial_split.sort(reverse=True)
        all_players = team1report.roster + team2report.roster
        all_players.sort(key=lambda p: p.kda(), reverse=True)
        for i in range(len(all_players)):
            all_players[i].runes_taken = round(runes_taken_total * (initial_split[i] / 100))

        # determine how many neutrals have spawned [5 spawn every minute; players will on average kill 50% of neutrals total]
        total_neutrals_spawned = self.duration_in_minutes * 5
        total_neutrals_killed = round(total_neutrals_spawned / 2)

        # determine how many neutrals were killed, split by players from both teams
        # same way as runes
        for i in range(len(initial_split)):
            chance = random.randint(0, 1)
            if chance == 1:
                change = random.randint(1, 5)
                initial_split[i] = initial_split[i] - change
                other_player_index = random.randint(0, len(initial_split) - 1)
                initial_split[other_player_index] = initial_split[other_player_index] + change
        initial_split.sort(reverse=True)
        for i in range(len(all_players)):
            all_players[i].neutrals_killed = round(total_neutrals_killed * (initial_split[i] / 100))

        # make cheaters
        for i in range(len(all_players)):
            if all_players[i].cheater:
                all_players[i].make_cheater()