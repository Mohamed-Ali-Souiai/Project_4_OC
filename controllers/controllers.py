from models.players import Players
from models.tournaments import Tournaments
from models.rounds import Rounds
from typing import List


NUMBER_OF_PLAYERS = 2


class Controllers:
    player_counter = 1

    def __init__(self, tournaments, view):
        self.players = []
        self.tournament_details = []
        self.tournaments = tournaments
        self.view = view

    def get_tournaments(self):
        name = self.view.enter_tournaments_name()
        venue = self.view.enter_tournaments_venue()
        date = self.view.enter_tournaments_date()
        remarks_director = self.view.enter_tournaments_remarks_director()
        self.tournament_details = Tournaments(name, venue, date, remarks_director)
        return self.tournament_details

    def get_players(self):
        for i in range(NUMBER_OF_PLAYERS):
            # while len(self.players) < 9:
            print()
            player_name = self.view.enter_player_name()
            player_first_name = self.view.enter_player_first_name()
            player_date_of_birth = self.view.enter_player_date_of_birth()
            player_sex = self.view.enter_player_sex()
            player_ranking = self.view.enter_player_ranking()
            player = Players(player_name, player_first_name,
                             player_date_of_birth, player_sex,
                             player_ranking
                             )
            self.players.append(player)
        return self.players

    def results_chess(self):
        pass

    def start_chess(self):
        pass

    def run(self):
        self.get_tournaments()
        self.get_players()
        print()
        self.view.show_players(self.get_players())
