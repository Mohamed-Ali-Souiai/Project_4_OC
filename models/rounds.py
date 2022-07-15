NUMBER_OF_ROUND = 4


class Rounds:

    def __init__(self):
        pass

    def sort_by_rating(self, list_players=[]):
        for i in range(len(list_players)):
            j = i
            while j > 0 and list_players[j-1].player_ranking > list_players[j].player_ranking:
                list_players[j-1].player_ranking, list_players[j].player_ranking = list_players[j].player_ranking, list_players[j-1].player_ranking
                j -= 1
        return list_players

    def first_rounds(self, list_players=[], list_rounds=[]):
        for i in range(4):
            list_rounds[i] = list_players[i],list_players[i+4]

    def next_round(self, list_players=[], list_rounds=[]):
        j = 0
        for i in range(2):
            list_rounds[i] = list_players[j], list_players[j + 1]
            j += 2
