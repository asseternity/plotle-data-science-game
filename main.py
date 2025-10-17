from team import Team
from role import Role
from player import Player
from generate_team_name import generate_team_name
from generate_player import generate_player
from match_outcome_determiner import Match

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

match1 = Match(team1, team2)
match1.print_report()
