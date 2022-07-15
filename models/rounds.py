from models.players import Players


class Rounds:
    def __init__(self, list_players=[]):
        self.players_round = list_players

    def sort_by_rating(self):
        self.players_round=sorted(self.players_round, key=self.players_round.player_ranking)

    def first_rounds(self):
        pass

    def next_round(self):
        pass
