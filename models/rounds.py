NUMBER_OF_ROUND = 4
HALF_NUMBER_OF_PLAYERS = 4


class Rounds:

    def __init__(self):
        pass

    def sort_by_rating(self, list_players):
        for i in range(len(list_players)):
            j = i
            while j > 0 and list_players[j-1].player_ranking > list_players[j].player_ranking:
                list_players[j-1], list_players[j] = list_players[j], list_players[j-1]
                j -= 1
        return list_players

    def first_rounds(self, list_players):
        """pair of players"""
        list_match = []
        for i in range(HALF_NUMBER_OF_PLAYERS):
            match = [list_players[i], list_players[i+4]]
            list_players[i].opponent_player.append(list_players[i+4].player_name)
            list_players[i+4].opponent_player.append(list_players[i].player_name)
            list_match.append(match)
        return list_match

    def next_rounds(self, list_players):
        list_match = []
        index = 0
        copy_list_players = list_players.copy()
        while len(copy_list_players) > 0:
            i = index
            if copy_list_players[index].player_name not in copy_list_players[i+1].opponent_player:
                match = [copy_list_players.pop(index), copy_list_players.pop(index)]
            elif copy_list_players[index].player_name not in copy_list_players[i+2].opponent_player:
                match = [copy_list_players.pop(index), copy_list_players.pop(index+1)]
            elif copy_list_players[index].player_name not in copy_list_players[i+3].opponent_player:
                match = [copy_list_players.pop(index), copy_list_players.pop(index+2)]
            else:
                match = [copy_list_players.pop(index), copy_list_players.pop(index+3)]
            list_match.append(match)
        return list_match
