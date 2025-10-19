class ConsoleGameFlow():
    def __init__(self):
        self.teams = []
        self.players_team = None

    def recruit_new_team():
        return

    def on_manage_roster():
        return

    def switch_player_roles(player1, player2):
        return

    def on_match_start():
        return

    def on_match_end():
        return
    
    def generate_player_string(self, player_stats):
        return f"{player_stats.player.username} | {player_stats.player.real_name} | {player_stats.role.value} | KDA: {player_stats.kills}-{player_stats.deaths}-{player_stats.assists} | Runes taken: {player_stats.runes_taken} | Neutrals killed: {player_stats.neutrals_killed}"

    def print_match_report(self, match):
        print(f"Winner: {match.winner.name} | Duration: {match.duration_in_minutes} mins")
        team_reports = [match.team1report, match.team2report]
        for team_report in team_reports:
            print("---------------------")
            print("TEAM:", team_report.team.name)
            for player_stats in team_report.player_stats:
                print(self.generate_player_string(player_stats))
            print("Total KDA:", f"{team_report.total_kills()}-{team_report.total_deaths()}-{team_report.total_assists()}")