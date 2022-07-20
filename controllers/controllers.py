from models.players import Players
from models.tournaments import Tournaments
from datetime import datetime


NUMBER_OF_PLAYERS = 8


class Controllers:
    player_counter = 1

    def __init__(self, rounds, view):
        self.players = []
        self.tournament_details = None
        self.rounds = rounds
        self.view = view

    def get_tournaments(self):
        date = []
        name = self.view.tournament_data("veuillez entrer le nom du tournois")
        venue = self.view.tournament_data("veuillez entrer le lieu du tournois")
        # date = self.view.tournament_data("veuillez entrer la date du tournois")
        date.append(datetime.today().strftime('%d-%m-%Y'))
        time_control = self.view.tournament_data("veuillez entrer le Controle du temps")
        remarks_director = self.view.tournament_data("veuillez entrer la remarque  du derecteur")
        self.tournament_details = Tournaments(name, venue, date,
                                              time_control, remarks_director
                                              )
        return self.tournament_details

    def get_players(self):
        for i in range(NUMBER_OF_PLAYERS):
            # while len(self.players) < 9:
            print()
            player_name = self.view.tournament_data("veuillez entrer le nom du joueur")
            player_first_name = self.view.tournament_data("veuillez entrer le prénom du joueur")
            player_date_of_birth = self.view.tournament_data("veuillez entrer la date de naissance du joueur")
            player_sex = self.view.tournament_data("veuillez entrer le sexe du joueur")
            player_ranking = self.view.tournament_data("veuillez entrer le classement du joueur")
            player = Players(player_name, player_first_name, player_date_of_birth, player_sex, player_ranking)
            self.players.append(player)
        return self.players

    def rounds_results(self, list_players):
        self.rounds.end_date_time = datetime.today().strftime('%d-%m-%Y %H:%M')
        player_points = []
        for i in range(NUMBER_OF_PLAYERS):
            player_points.append(
                self.view.tournament_data(f"veuillez entrer le score du {list_players[i].player_name}")
            )

    def start_round(self,):
        """retourne """
        self.rounds.rounds_name = self.view.tournament_data("veuillez entrer le nom de la tours")
        self.rounds.date_start_time = datetime.today().strftime('%d-%m-%Y %H:%M')
        next_rounds = ["rounds2", "rounds3", "rounds4"]
        if self.rounds.rounds_name == "rounds1":
            self.players = self.rounds.sort_by_rating(self.players)
            list_match = self.rounds.first_rounds(self.players)
            return list_match
        elif self.rounds.rounds_name in next_rounds:
            list_match = self.rounds.next_rounds(self.players)
            return list_match
        else:
            return None

    def start_tournament(self):
        menu = self.view.show_menu()
        if menu == '1':
            self.tournament_details = self.get_tournaments()
            self.players = self.get_players()
        elif menu == '2':
            self.start_round()
        elif menu == '3':
            self.rounds_results(self.players)
        self.start_round()

        #self.players = self.rounds.sort_by_rating(self.players)
        #self.view.show_details_tournament(tournament)
        # self.view.show_players(self.players)
