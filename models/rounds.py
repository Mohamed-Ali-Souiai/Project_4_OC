from models.match import Match

START_SCORE = 0
NUMBER_PLAYERS = 8
HALF_NUMBER_OF_PLAYERS = 4


class Rounds:

    def __init__(self):
        self.rounds_name = ''
        self.date_start_time = ''
        self.date_end_time = ''
        self.list_match = []
        self.match = Match()

    def __str__(self):
        """Used in print."""
        return f"\nNom de la tours:{self.rounds_name}\n" \
               f"Date debut:{self.date_start_time}\n" \
               f"Date fin:{self.date_end_time}\n" \
               f"liste des matchs:{self.list_match}\n"

    def __repr__(self):
        """Used in print."""
        return str(self)

    def __getitem__(self, item):
        return self.__dict__[item]

    def rounds_table(self):
        """serialize the object"""
        dict_rounds = {
            'rounds_name': self.rounds_name,
            'date_start_time': self.date_start_time,
            'date_end_time': self.date_end_time,
            'list_match': self.list_match
        }
        return dict_rounds

    def sort_by_rating(self, list_players):
        """" returns list of players sorted by rating"""
        for i in range(len(list_players)):
            j = i
            while j > 0 and list_players[j-1].player_ranking > list_players[j].player_ranking:
                list_players[j-1], list_players[j] = list_players[j], list_players[j-1]
                j -= 1
        return list_players

    def sort_by_point(self, list_players):
        """returns list of players sorted by point"""
        for i in range(len(list_players)):
            j = i
            while j > 0 and list_players[j-1].total_points <= list_players[j].total_points:
                if list_players[j-1].total_points < list_players[j].total_points:
                    list_players[j-1], list_players[j] = list_players[j], list_players[j-1]
                elif list_players[j-1].player_ranking > list_players[j].player_ranking:
                    list_players[j - 1], list_players[j] = list_players[j], list_players[j - 1]
                j -= 1
        return list_players

    def first_rounds(self, list_players):
        """returns the pair of round players """
        self.list_match = []
        for i in range(HALF_NUMBER_OF_PLAYERS):
            pair = [list_players[i], list_players[i+4]]
            list_players[i].opponent_player.append(list_players[i+4].player_name)
            list_players[i+4].opponent_player.append(list_players[i].player_name)
            self.list_match.extend(pair)
        return self.list_match

    def next_rounds(self, list_players):
        # a refaire
        """returns list of round matches '2 3 4'. """
        self.list_match = []
        for i in range(len(list_players)-1):
            if i in [1, 3, 5, 7]:
                continue
            j = i
            while j < len(list_players)-1:
                if list_players[j].player_name in list_players[j+1].opponent_player:
                    j += 1
                else:
                    list_players[j], list_players[j+1] = list_players[j+1], list_players[j]
                    break
            list_players[i].opponent_player.append(list_players[i + 1].player_name)
            list_players[i + 1].opponent_player.append(list_players[i].player_name)
        self.list_match = list_players
        """index = 0
        copy_list_players = list_players.copy()
        while len(copy_list_players) > 0:
            if copy_list_players[index].player_name not in copy_list_players[index+1].opponent_player:
                pair = [copy_list_players.pop(index), copy_list_players.pop(index)]
            elif copy_list_players[index].player_name not in copy_list_players[index+2].opponent_player \
                    and len(copy_list_players) > 1:
                pair = [copy_list_players.pop(index), copy_list_players.pop(index+1)]
            elif copy_list_players[index].player_name not in copy_list_players[index+3].opponent_player \
                    and len(copy_list_players) > 2:
                pair = [copy_list_players.pop(index), copy_list_players.pop(index+2)]
            elif copy_list_players[index].player_name not in copy_list_players[index+4].opponent_player \
                    and len(copy_list_players) > 3:
                pair = [copy_list_players.pop(index), copy_list_players.pop(index+3)]
            else:
                pair = [copy_list_players.pop(index), copy_list_players.pop(index)]
            self.list_match.extend(pair)"""
        return self.list_match

    def rounds_results(self, list_players, score):
        """retourne liste des match de la tours"""
        self.list_match = []
        for i in range(NUMBER_PLAYERS):
            if i in [1, 3, 5, 7]:
                continue
            first_player = self.match.player_score(list_players[i], score[i])
            second_player = self.match.player_score(list_players[i + 1], score[i + 1])
            pair = self.match.player_pair(first_player, second_player)
            self.list_match.append(pair)
        return self.list_match

