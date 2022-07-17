from models.players import Players
from models.tournaments import Tournaments


NUMBER_OF_PLAYERS = 2


class Controllers:
    player_counter = 1

    def __init__(self, rounds, view):
        self.players = []
        self.tournament_details = []
        self.rounds = rounds
        self.view = view

    def get_tournaments(self):
        name = self.view.tournament_data("veuillez entrer le nom du tournois")
        venue = self.view.tournament_data("veuillez entrer le lieu du tournois")
        date = self.view.tournament_data("veuillez entrer la date du tournois")
        time_control = self.view.tournament_data("veuillez entrer le Controle du temps")
        remarks_director = self.view.tournament_data("veuillez entrer la remarque  du derecteur")
        self.tournament_details = Tournaments(name, venue,
                                              date, time_control,
                                              remarks_director
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
            player = Players(player_name, player_first_name,
                             player_date_of_birth, player_sex,
                             player_ranking
                             )
            self.players.append(player)
        return self.players

    def results_chess(self):
        first_player_point = self.view.tournament_data("veuillez entrer le score du premier joueur")
        second_player_point = self.view.tournament_data("veuillez entrer le nom du deuxieme joueur")
        return first_player_point, second_player_point

    def start_chess(self):
        pass

    def run(self):
        self.get_tournaments()
        self.get_players()
        self.players = self.rounds.sort_by_rating(self.players)
        self.view.show_players(self.players)
