from models.match import Match

START_SCORE = 0
NUMBER_OF_ROUND = 4
HALF_NUMBER_OF_PLAYERS = 4


class Rounds:

    def __init__(self):
        self.rounds_name = ''
        self.date_start_time = ''
        self.date_end_time = ''
        self.list_match = []
        self.match = Match()

    def sort_by_rating(self, list_players):
        for i in range(len(list_players)):
            j = i
            while j > 0 and list_players[j-1].player_ranking > list_players[j].player_ranking:
                list_players[j-1], list_players[j] = list_players[j], list_players[j-1]
                j -= 1
        return list_players

    def sort_by_point(self, list_players):
        for i in range(len(list_players)):
            j = i
            while j > 0 and list_players[j-1].player_score < list_players[j].player_score:
                list_players[j-1], list_players[j] = list_players[j], list_players[j-1]
                j -= 1
        return list_players

    def first_rounds(self, list_players):
        """pair of players"""
        for i in range(HALF_NUMBER_OF_PLAYERS):
            first_player = self.match.player_score(list_players[i], START_SCORE)
            second_player = self.match.player_score(list_players[i+4], START_SCORE)
            pair = self.match.pair_generation(first_player, second_player)
            """[list_players[i], list_players[i+4]]"""
            """list_players[i].opponent_player.append(list_players[i+4].player_name)
            list_players[i+4].opponent_player.append(list_players[i].player_name)"""
            self.list_match.append(pair)
        return self.list_match

    def next_rounds(self, list_players):
        # a refaire
        """retoune liste des match des rounds 2 3 4"""
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
            list_match.extend(match)
        return list_match
