import random


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def ranking(self):
        pass

    def set_results(self):
        pass

    def set_score(self):
        pass

    def shuffle(self, color):
        random.shuffle(color)

    """def match(self):
        if self.player1.get_score()>self.player2.get_score():
            pass
        match_unique = (self.list_player1, self.list_player2)
        return match_unique"""
