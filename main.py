from team_name_generator import generate_team_name
from username_generator import generate_username
from player_report_class import PlayerReportCard, Role

print("---- TEAM LIGHT ----")
print ("Team name:", generate_team_name())
print("1.", PlayerReportCard(generate_username(), Role.WARRIOR).string())
print("2.", PlayerReportCard(generate_username(), Role.MARKSMAN).string())
print("3.", PlayerReportCard(generate_username(), Role.SUPPORT).string())
print("4.", PlayerReportCard(generate_username(), Role.MAGE).string())
print("5.", PlayerReportCard(generate_username(), Role.ASSASSIN).string())

print("---- TEAM DARK ----")
print ("Team name:", generate_team_name())
print("1.", PlayerReportCard(generate_username(), Role.WARRIOR).string())
print("2.", PlayerReportCard(generate_username(), Role.MARKSMAN).string())
print("3.", PlayerReportCard(generate_username(), Role.SUPPORT).string())
print("4.", PlayerReportCard(generate_username(), Role.MAGE).string())
print("5.", PlayerReportCard(generate_username(), Role.ASSASSIN).string())