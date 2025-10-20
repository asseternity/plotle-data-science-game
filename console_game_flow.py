from generate_player import generate_player
from generate_team import generate_team
from match_outcome_determiner import Match
from role import Role
from team import Team

class ConsoleGameFlow():
    def __init__(self):
        self.teams = []
        self.players_team = None

        # Game Start
        print("You started a new esports organization, centered around a popular MOBA game, Teamfight.")
        print("What is the name of your team?")
        user_input_team_name = input("Please input team name: ")

        print("Now, you need players. You send word out and find some potential recruits.")
        starting_team_roster = []
        recruits_pool = self.present_new_recruits()

        while len(starting_team_roster) < 5:
            print(f"Please enter the number of the recruit you'd like to add to the {user_input_team_name} roster.")
            user_input_new_recruit = int(input("Please input recruit number: "))
            if recruits_pool[user_input_new_recruit - 1] != None:
                starting_team_roster.append(recruits_pool[user_input_new_recruit - 1])
                print(f"You have added {recruits_pool[user_input_new_recruit - 1].username} to {user_input_team_name}.")
            else:
                print("Invalid recruit number")

        print(f"Now you have a full squad. The {user_input_team_name} are looking strong:")
        for player in starting_team_roster:
            print(f"{player.username}")

        players_team = Team(user_input_team_name, *starting_team_roster)
        self.main_menu(players_team)

    def main_menu(self, team):
        print("------- MAIN MENU --------")
        self.print_roster(team)
        print("--------------------------")

        # Check if all player roles are filled
        unassigned_players = [p for p in team.roster if not hasattr(p, "current_role") or p.current_role is None]
        if unassigned_players:
            print("⚠️ Warning: Some players do not have assigned roles!")
            for p in unassigned_players:
                print(f" - {p.username}")
            print()

        # Check if IGL is assigned
        if not hasattr(team, "igl") or team.igl is None:
            print("⚠️ Warning: No IGL assigned.\n")

        # Display next opponent (placeholder for now)
        next_opponent = generate_team()
        print(f"Next opponent: 🆚 {next_opponent.name}\n")

        # 4️⃣ List of possible actions
        print("Available actions:")
        print("1. Change player roles")
        print("2. Appoint IGL")
        print("3. Proceed to next match")

        while True:
            try:
                choice = int(input("Enter command number: "))
                if choice == 1:
                    self.handle_change_roles(team)
                elif choice == 2:
                    self.handle_appoint_igl(team)
                elif choice == 3:
                    # Check prerequisites before proceeding
                    unassigned_players = [p for p in team.roster if not hasattr(p, "current_role") or p.current_role is None]
                    if unassigned_players:
                        print("🚫 You cannot start a match until all players have roles assigned!\n")
                        for p in unassigned_players:
                            print(f" - {p.username} has no role assigned.")
                        continue  # Go back to menu loop
                    print(f"\n🏁 Starting match against {next_opponent.name}...\n")
                    self.on_match_start(team, next_opponent)
                    break
                else:
                    print("Invalid choice. Please enter 1–3.")
            except ValueError:
                print("Please enter a number (1–3).")

    def present_new_recruits(self):
        recruits = []
        for i in range(25):
            print("------------------------")
            print(f"Player number {i + 1}:")
            new_player = generate_player()
            recruits.append(new_player)
            self.print_player_profile(new_player)
        return recruits

    def handle_appoint_igl(self, team):
        print("\n--- Appoint IGL ---")
        print("Choose a player to become the In-Game Leader (IGL):")
        for i, player in enumerate(team.roster, start=1):
            print(f"{i}. {player.username} (Leadership: {player.leadership})")

        try:
            choice = int(input("Enter the number of the player to appoint as IGL: "))
            if 1 <= choice <= len(team.roster):
                chosen_player = team.roster[choice - 1]
                team.igl = chosen_player
                print(f"🎖️ {chosen_player.username} has been appointed as the IGL of {team.name}!\n")
            else:
                print("❌ Invalid selection. Please enter a valid player number.")
        except ValueError:
            print("❌ Please enter a number.")
        return team

    def handle_change_roles(self, team):
        print("\n--- Change Player Roles ---")
        print("Current roster and roles:")
        for i, player in enumerate(team.roster, start=1):
            role = getattr(player.current_role, "value", "Unassigned")
            print(f"{i}. {player.username} — Role: {role}")

        try:
            player_index = int(input("Enter the number of the player you want to assign/change role for: ")) - 1
            if not (0 <= player_index < len(team.roster)):
                print("❌ Invalid player number.")
                return team

            # Show available roles
            print("\nAvailable roles:")
            for i, role in enumerate(Role, start=1):
                print(f"{i}. {role.value}")

            role_choice = int(input("Enter the number of the role to assign: ")) - 1
            if not (0 <= role_choice < len(Role)):
                print("❌ Invalid role selection.")
                return team

            selected_player = team.roster[player_index]
            chosen_role = list(Role)[role_choice]

            # Attempt to assign role
            success = selected_player.set_role_if_unoccupied(chosen_role)
            if success:
                print(f"✅ {selected_player.username} is now assigned to the {chosen_role.value} role.")
            else:
                print(f"🚫 The {chosen_role.value} role is already occupied by another player.")

        except ValueError:
            print("❌ Please enter valid numbers for player and role.")
        return team

    def on_match_start(self, team1, team2):
        match = Match(team1, team2)
        print("---------------")
        print(f"Match between {team1.name} and {team2.name}.")
        self.print_match_report_full(match)
        print('----------------')
        self.main_menu(team1)
        return
    
    def print_player_profile(self, player):
        print(f"{player.username} | {player.real_name} | Age: {player.age} | Gender: {player.gender} | Attack skill: {player.attack} | Defense skill: {player.defense} | Leadership: {player.leadership}")
    
    def print_roster(self, team):
        print(f"Team: {team.name}")
        for player in team.roster:
            print(f"{player.username} | {player.real_name} | Role: {player.get_role_name()} Age: {player.age} | Gender: {player.gender} | Attack skill: {player.attack} | Defense skill: {player.defense} | Leadership: {player.leadership}")
        print(f"IGL: {team.get_igl()}")
    
    def print_match_report_full(self, match):
        print(f"Winner: {match.winner.name} | Duration: {match.duration_in_minutes} mins")
        team_reports = [match.team1report, match.team2report]
        for team_report in team_reports:
            print("---------------------")
            print("TEAM:", team_report.team.name)
            for player_stats in team_report.player_stats:
                print(f"{player_stats.player.username} | {player_stats.player.real_name} | {player_stats.role.value} | KDA: {player_stats.kills}-{player_stats.deaths}-{player_stats.assists} | Runes taken: {player_stats.runes_taken} | Neutrals killed: {player_stats.neutrals_killed}")
            print("Total KDA:", f"{team_report.total_kills()}-{team_report.total_deaths()}-{team_report.total_assists()}")
