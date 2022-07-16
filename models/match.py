import random


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def set_results(self):
        pass

    def meeting_discuss_between_players(self):
        pass

    def set_score(self, first_player, second_player):
        match_unique = first_player, second_player
        return match_unique

    def shuffle(self, color):
        random.shuffle(color)
