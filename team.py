class Team():
    def __init__(self, name, player1, player2, player3, player4, player5):
        self.name = name
        self.roster = [player1, player2, player3, player4, player5]
        self.igl = None

        for player in self.roster:
            player.team = self

        # league vars
        self.latest_match = None
        self.next_opponent = None
        self.season_match_history = []
        self.league_position = None
        self.season_wins = 0
        self.season_losses = 0
        self.past_league_results = []

    def shuffle_roster(self, player1, player2):
        if player1 in self.roster:
            self.roster.remove(player1)
            self.roster.append(player2)
            player2.team = player1.team
            player1.team = None
            return True
        return False
    
    def get_igl(self):
        return self.igl.username if self.igl else "Unassigned"

    def appoint_igl(self, player):
        if player in player.roster:
            self.igl = player