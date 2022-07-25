class Match:
    def __init__(self, score, player):
        self.score = score
        self.player = player

    def player_score(self):
        return [self.player, self.score]


