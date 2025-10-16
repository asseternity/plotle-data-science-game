from team_report_class import TeamReportCard

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
        