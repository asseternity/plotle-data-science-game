from generate_team_name import generate_team_name
from generate_player import generate_player
from team import Team
from role import Role

def generate_team():
    team_name = generate_team_name()
    roster = []
    for i in range(5):
        new_player = generate_player()
        roster.append(new_player)

    roster[0].current_role = Role.WARRIOR
    roster[1].current_role = Role.MARKSMAN
    roster[2].current_role = Role.MAGE
    roster[3].current_role = Role.ASSASSIN
    roster[4].current_role = Role.SUPPORT
    
    new_team = Team(team_name, *roster)

    new_team.igl = new_team.roster[0]

    return new_team
