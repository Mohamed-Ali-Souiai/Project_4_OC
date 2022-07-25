class Match:
    def __init__(self, score, player):
        self.score = score
        self.player = player

    def player_score(self):
        return [self.player, self.score]

    def match_score(self, first_player, second_player):
        return first_player, second_player
