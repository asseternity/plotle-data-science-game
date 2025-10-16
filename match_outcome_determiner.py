from team_report_class import TeamReportCard

class Match():
    def __init__(self, team1report: TeamReportCard, team2report: TeamReportCard):
        self.team1report = team1report
        self.team2report = team2report
        self.winner = None
        self.duration_in_minutes = None

        team1KDA = team1report.total_kills() + team1report.total_assists() - team1report.total_deaths()
        team2KDA = team2report.total_kills() + team2report.total_assists() - team2report.total_deaths()
        KDA_difference = team1KDA - team2KDA
        if KDA_difference > 0:
            self.winner = team1report
        else:
            self.winner = team2report

        all_actions = team1report.total_kills() + team1report.total_assists() + team1report.total_deaths() + team2report.total_kills() + team2report.total_assists() + team2report.total_deaths()
        self.duration_in_minutes = round(all_actions / 5)
        