from team import Team
from role import Role
from player import Player
from generate_username import generate_username
from generate_team_name import generate_team_name
from match_outcome_determiner import Match

a1 = Player("ylari_x", "X", "X", "X", Role.WARRIOR, 4, 0)
a2 = Player(generate_username(), "X", "X", "X", Role.MARKSMAN, 0, 0)
a3 = Player(generate_username(), "X", "X", "X", Role.MAGE, 0, 0)
a4 = Player(generate_username(), "X", "X", "X", Role.ASSASSIN, 0, 0)
a5 = Player(generate_username(), "X", "X", "X", Role.SUPPORT, 0, 0)

b1 = Player("queen_fufu", "X", "X", "X", Role.WARRIOR, 0, 4)
b2 = Player(generate_username(), "X", "X", "X", Role.MARKSMAN, 0, 0)
b3 = Player(generate_username(), "X", "X", "X", Role.MAGE, 0, 0)
b4 = Player(generate_username(), "X", "X", "X", Role.ASSASSIN, 0, 0)
b5 = Player(generate_username(), "X", "X", "X", Role.SUPPORT, 0, 0)

team1 = Team(generate_team_name(), a1, a2, a3, a4, a5)
team2 = Team(generate_team_name(), b1, b2, b3, b4, b5)
match1 = Match(team1, team2)
match1.print_report()
