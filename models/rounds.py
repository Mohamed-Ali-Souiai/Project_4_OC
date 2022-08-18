"""Define rounds"""
from models.match import Match
from random import choice

START_SCORE = 0
NUMBER_PLAYERS = 8
HALF_NUMBER_OF_PLAYERS = 4


class Rounds:

    def __init__(self):
        self.rounds_name = ''
        self.date_start_time = ''
        self.date_end_time = ''
        self.results = {}
        self.list_match = []
        self.match = Match()

    def draw(self):
        """drawing of lot"""
        color_list = []
        for i in range(NUMBER_PLAYERS):
            if i in [1, 3, 5, 7]:
                continue
            color = choice(['black', 'white'])
            if color == 'black':
                color_list.append(['black', 'white'])
            else:
                color_list.append(['white', 'black'])
        return color_list

    def __str__(self):
        """Used in print."""
        return (
            f"\nNom de la tours:{self.rounds_name}\n"
            f"Date debut:{self.date_start_time}\n"
            f"Date fin:{self.date_end_time}\n"
            f"results:{self.results}\n"
            f"liste des matchs:{self.list_match}\n"
        )

    def __repr__(self):
        """Used in print."""
        return str(self)

    def __getitem__(self, item):
        """Used in print."""
        return self.__dict__[item]

    def rounds_table(self):
        """serialize the object"""
        dict_rounds = {
            'rounds_name': self.rounds_name,
            'date_start_time': self.date_start_time,
            'date_end_time': self.date_end_time,
            'results': self.results,
            'list_match': self.list_match
        }
        return dict_rounds

    def sort_by_rating(self, list_players):
        """" returns list of players sorted by rating"""
        for i in range(len(list_players)):
            j = i
            while j > 0 and list_players[j-1].ranking > list_players[j].ranking:
                list_players[j-1], list_players[j] = \
                    list_players[j], list_players[j-1]
                j -= 1
        return list_players

    def sort_by_point(self, list_players):
        """returns list of players sorted by point"""
        for i in range(len(list_players)):
            j = i
            while j > 0 and list_players[j-1].total_points <= list_players[j].total_points:
                if list_players[j-1].total_points < list_players[j].total_points:
                    list_players[j-1], list_players[j] = list_players[j], list_players[j-1]
                elif list_players[j-1].ranking > list_players[j].ranking:
                    list_players[j - 1], list_players[j] = list_players[j], list_players[j - 1]
                j -= 1
        return list_players

    def list_pair(self, list_players):
        """return player pair list"""
        player_pair_list = []
        for i in range(NUMBER_PLAYERS):
            if i in [1, 3, 5, 7]:
                continue
            pair = list(
                self.match.player_pair(list_players[i], list_players[i+1])
            )
            player_pair_list.append(pair)
        return player_pair_list

    def first_rounds(self, list_players):
        """returns the pair of round players """
        self.list_match = []
        for i in range(HALF_NUMBER_OF_PLAYERS):
            pair = [list_players[i], list_players[i+4]]
            list_players[i].opponent.append(list_players[i+4].name)
            list_players[i+4].opponent.append(list_players[i].name)
            self.list_match.extend(pair)
        return self.list_match

    def next_rounds(self, list_players):
        """returns list of round matches '2 3 4'. """
        self.list_match = []
        for i in range(len(list_players)-1):
            if i in [1, 3, 5, 7]:
                continue
            j = i
            while j < len(list_players)-1:
                if list_players[j].name in list_players[j+1].opponent:
                    j += 1
                else:
                    list_players[j], list_players[j+1] = list_players[j+1], list_players[j]
                    break
            list_players[i].opponent.append(list_players[i + 1].name)
            list_players[i + 1].opponent.append(list_players[i].name)
        self.list_match = list_players
        return self.list_match

    def rounds_results(self, list_players, score):
        """retourne liste des match de la tours"""
        players = list_players.copy()
        self.list_match = []
        for i in range(NUMBER_PLAYERS):
            if i in [1, 3, 5, 7]:
                continue
            first_player = self.match.player_score(players[i], score[i])
            second_player = self.match.player_score(
                players[i + 1], score[i + 1]
            )
            pair = self.match.player_pair(first_player, second_player)
            self.list_match.append(pair)
        return self.list_match
