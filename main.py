from team import Team
from role import Role
from player import Player
from generate_team_name import generate_team_name
from generate_player import generate_player
from match_outcome_determiner import Match
from data_head_to_head import head_to_head_stats

a1 = Player("ylari_x", "X", "X", "X", Role.WARRIOR, 5, 0)
a1.leadership = 5
a2 = generate_player(Role.MARKSMAN)
a3 = generate_player(Role.MAGE)
a4 = generate_player(Role.ASSASSIN)
a5 = generate_player(Role.SUPPORT)
team1 = Team(generate_team_name(), a1, a2, a3, a4, a5)
team1.igl = a1

b1 = Player("queen_fufu", "X", "X", "X", Role.WARRIOR, 0, 15)
b2 = generate_player(Role.MARKSMAN)
b3 = generate_player(Role.MAGE)
b4 = generate_player(Role.ASSASSIN)
b5 = generate_player(Role.SUPPORT)
team2 = Team(generate_team_name(), b1, b2, b3, b4, b5)

for i in range(100):
    Match(team1, team2)

team1_vs_team2_stats = head_to_head_stats(team1, team2)

print(team1_vs_team2_stats["team_stats"])
print(team1_vs_team2_stats["player_stats"])