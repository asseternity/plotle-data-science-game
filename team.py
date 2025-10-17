class Team():
    def __init__(self, name, player1, player2, player3, player4, player5):
        self.name = name
        self.roster = [player1, player2, player3, player4, player5]
        self.igl = None
        self.latest_match = None
        self.match_history = []

        for player in self.roster:
            player.team = self

    def appoint_igl(self, player):
        if player in player.roster:
            self.igl = player