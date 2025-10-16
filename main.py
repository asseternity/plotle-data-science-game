from team_report_class import TeamReportCard
from match_outcome_determiner import Match

team1 = TeamReportCard()
team2 = TeamReportCard()
match = Match(team1, team2)
print(f"Winner: {match.winner.name} | Duration: {match.duration_in_minutes} mins")
team1.print_report()
team2.print_report()
