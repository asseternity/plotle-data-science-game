class Team():
    def __init__(self, name, player1, player2, player3, player4, player5):
        self.name = name
        self.roster = [player1, player2, player3, player4, player5]
        self.latest_match = None
        self.match_history = []