import random
from match_outcome_determiner import Match

class League():
    def __init__(self, name, teams):
        # throw if number of teams is odd
        if len(teams) % 2 != 0:
            raise ValueError("Number of teams must be even to schedule matches properly.")

        self.name = name
        self.teams = teams
        self.matches_per_season = (len(self.teams) - 1) * 2
        self.next_pairs = []
        self.league_over = False

    def determine_next_pairs(self):
        if len(self.teams[0].season_match_history) == self.matches_per_season:
            self.league_over = True
            return
        
        self.next_pairs = []
        available_teams = self.teams.copy()
        random.shuffle(available_teams)
        
        while available_teams:
            team1 = available_teams.pop()
            team2 = available_teams.pop()
            self.next_pairs.append((team1, team2))
            team1.next_opponent = team2
            team2.next_opponent = team1
    
    def proceed(self):
        if self.league_over:
            self.finish_league()
        else:
            self.run_matches()
    
    def run_matches(self):
        for pair in self.next_pairs:
            Match(pair[0], pair[1])

    def update_league_positions(self):
        self.teams.sort(key=lambda team: team.season_wins, reverse=True)
    
    def finish_league(self):
        # remove match histories of teams, but not players
        return
