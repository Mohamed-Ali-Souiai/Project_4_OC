from models.players import Players


class Rounds:
    def __init__(self):
        pass

    def sort_by_rating(self, list_players=[]):
        for i in range(len(list_players)):
            j=i
            while j>0 and list_players[j-1].player_ranking > list_players[j].player_ranking:
                list_players[j-1].player_ranking, list_players[j].player_ranking = list_players[j].player_ranking, list_players[j-1].player_ranking
                j -= 1

    def first_rounds(self):
        pass

    def next_round(self):
        pass
