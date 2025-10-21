from generate_player import generate_player
from generate_team import generate_team
from match_outcome_determiner import Match
from league import League
from role import Role
from team import Team

class ConsoleGameFlow():
    def __init__(self):
        # Create player's team
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

        self.players_team = Team(user_input_team_name, *starting_team_roster)
        

        # League creation        
        teams = []
        for i in range (7):
            team = generate_team()
            teams.append(team)
        teams.append(self.players_team)

        self.league = League("Teamfight Pro League", teams)

        # Start game
        self.main_menu()

    def main_menu(self):
        team = self.players_team
        print("------- MAIN MENU --------")
        self.print_roster(self.players_team)
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

        # Display league info
        self.league.determine_next_pairs()
        self.league.update_league_positions()
        print("-------------")
        for i, team in enumerate(self.league.teams, start=1):
            print(f"{i}. {team.name} | {team.season_wins} - {team.season_losses}")

        if self.players_team.next_opponent != None:
            next_opponent = self.players_team.next_opponent.name
            print(f"Next opponent: 🆚 {next_opponent}\n")
        else:
            print(f"Next: 🏆 season recap\n")

        while True:
            try:
                # List of possible actions
                self.print_main_menu_actions()
                choice = int(input("Enter command number: "))
                if choice == 1:
                    self.handle_change_roles()
                elif choice == 2:
                    self.handle_appoint_igl()
                elif choice == 3:
                    # Check prerequisites before proceeding
                    unassigned_players = [p for p in team.roster if not hasattr(p, "current_role") or p.current_role is None]
                    if unassigned_players:
                        print("🚫 You cannot start a match until all players have roles assigned!\n")
                        for p in unassigned_players:
                            print(f" - {p.username} has no role assigned.")
                        continue  # Go back to menu loop
                    print(f"\n🏁 Starting match against {next_opponent}...\n")
                    self.handle_proceed()
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

    def handle_appoint_igl(self):
        print("\n--- Appoint IGL ---")
        print("Choose a player to become the In-Game Leader (IGL):")
        for i, player in enumerate(self.players_team.roster, start=1):
            print(f"{i}. {player.username} (Leadership: {player.leadership})")

        try:
            choice = int(input("Enter the number of the player to appoint as IGL: "))
            if 1 <= choice <= len(self.players_team.roster):
                chosen_player = self.players_team.roster[choice - 1]
                self.players_team.igl = chosen_player
                print(f"🎖️ {chosen_player.username} has been appointed as the IGL of {self.players_team.name}!\n")
            else:
                print("❌ Invalid selection. Please enter a valid player number.")
        except ValueError:
            print("❌ Please enter a number.")
        return self.players_team

    def handle_change_roles(self):
        print("\n--- Change Player Roles ---")
        print("Current roster and roles:")
        for i, player in enumerate(self.players_team.roster, start=1):
            role = getattr(player.current_role, "value", "Unassigned")
            print(f"{i}. {player.username} — Role: {role}")

        try:
            player_index = int(input("Enter the number of the player you want to assign/change role for: ")) - 1
            if not (0 <= player_index < len(self.players_team.roster)):
                print("❌ Invalid player number.")
                return self.players_team

            # Show available roles
            print("\nAvailable roles:")
            for i, role in enumerate(Role, start=1):
                print(f"{i}. {role.value}")

            role_choice = int(input("Enter the number of the role to assign: ")) - 1
            if not (0 <= role_choice < len(Role)):
                print("❌ Invalid role selection.")
                return self.players_team

            selected_player = self.players_team.roster[player_index]
            chosen_role = list(Role)[role_choice]

            # Attempt to assign role
            success = selected_player.set_role_if_unoccupied(chosen_role)
            if success:
                print(f"✅ {selected_player.username} is now assigned to the {chosen_role.value} role.")
            else:
                print(f"🚫 The {chosen_role.value} role is already occupied by another player.")

        except ValueError:
            print("❌ Please enter valid numbers for player and role.")
        return self.players_team
    
    def handle_proceed(self):
        if self.league.league_over == True:
            self.season_recap()
        else:
            self.league.run_matches()
            self.on_match_start()

    def on_match_start(self):
        match = self.players_team.season_match_history[len(self.players_team.season_match_history) - 1]
        print("---------------")
        print(f"Match between {self.players_team.name} and {self.players_team.next_opponent.name}.")
        self.print_match_report_full(match)
        print('----------------')
        self.main_menu()
        return
    
    def season_recap(self):
        print("------------------")
        print("Final League Standings")
        for i, team in enumerate(self.league.teams, start=1):
            print(f"{i}. {team.name} | {team.season_wins} - {team.season_losses}")
        self.post_season_shuffle()
    
    def post_season_shuffle(self):
        print("---------------")
        print("This is a chance for you to do shuffles to your team.")
        print("Do you want to do reshuffles to your roster? 1 - Yes, 2 - No")
        user_wants_reshuffles = int(input("Please input response number: "))
        if user_wants_reshuffles == 2:
            return self.main_menu()
        else:
            recruits_pool = self.present_new_recruits()
            player_satisfied = False    
            while not player_satisfied:
                try:
                    print(f"Please enter the number of the recruit you'd like to add to the {self.players_team.name} roster.")
                    user_input_new_recruit = int(input("Please input recruit number: "))
                    if not (1 <= user_input_new_recruit <= len(recruits_pool)):
                        print("❌ Invalid recruit number.")
                        continue
                    chosen_recruit = recruits_pool[user_input_new_recruit - 1]
                    if chosen_recruit is None:
                        print("❌ That recruit has already been chosen.")
                        continue
                    for i, player in enumerate(self.players_team.roster, start=1):
                        print(f"{i}. {player.username} | {player.real_name} | Age: {player.age} | Gender: {player.gender} | Attack skill: {player.attack} | Defense skill: {player.defense} | Leadership: {player.leadership}")
                    print("Please indicate who should be kicked from the roster")
                    user_kicks = int(input("Please input player number: "))
                    if 0 < user_kicks < 6:
                        kicked_player = self.players_team.roster[user_kicks - 1]
                        self.players_team.shuffle_roster(kicked_player, chosen_recruit) 
                        print(f"You have added {chosen_recruit.username} and removed {kicked_player.username}.")
                        recruits_pool[user_input_new_recruit - 1] = None
                        print("Do you want to do more reshuffles? 1 - Yes, 2 - No")
                        user_satisfaction = int(input("Enter response number: "))
                        if (user_satisfaction) == 2:
                            player_satisfied = True
                    else:
                        print("Invalid player number.")
                except ValueError:
                    print("❌ Please enter a valid number.")
            return self.main_menu()

    def print_main_menu_actions(self):        
        print("Available actions:")
        print("1. Change player roles")
        print("2. Appoint IGL")
        print("3. Proceed to next match")
    
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
