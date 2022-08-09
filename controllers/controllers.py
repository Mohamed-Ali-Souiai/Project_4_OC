"""Define the main controller."""

from tinydb import TinyDB, Query
from datetime import datetime

from models.players import Players

NUMBER_PLAYERS = 8
NUMBER_ROUNDS = 4


class Controllers:
    """Main controller."""

    def __init__(self, tournaments, rounds, view):
        self.players = []
        self.rounds = rounds
        self.view = view
        self.tournaments = tournaments
        # self.tournament_details = Tournaments()

    def control_date(self, date):
        """retourne une date valide"""
        try:
            datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            print('date non valide')
            return None
        return date

    def get_tournaments(self):
        """retourne les details de la tournois"""
        self.tournaments.tournaments_name = self.view.tournament_data(
            "veuillez entrer le nom du tournois: "
        )
        self.tournaments.tournaments_venue = self.view.tournament_data(
            "veuillez entrer le lieu du tournois: "
        )
        self.tournaments.tournaments_date.append(datetime.today().strftime('%d-%m-%Y'))
        self.tournaments.time_control = self.view.tournament_data(
            "veuillez entrer le Controle du temps: "
        )
        self.tournaments.remarks_director.append(
            self.view.tournament_data(
                "veuillez entrer la remarque  du directeur: "
            )
        )

    def get_players(self):
        """retourne la liste des jouers"""
        condition = True
        for i in range(NUMBER_PLAYERS):
            # while len(self.players) < 9:
            print()
            player_name = self.view.tournament_data(
                f"veuillez entrer le nom du joueur n°{i+1}: "
            )
            player_first_name = self.view.tournament_data(
                f"veuillez entrer le prénom du joueur n°{i+1}: "
            )
            while condition:
                player_date_of_birth = self.view.tournament_data(
                    f"veuillez entrer la date de naissance du joueur n°{i+1}: "
                )
                if self.control_date(player_date_of_birth):
                    break

            while condition:
                player_sex = self.view.tournament_data(
                    f"veuillez entrer le sexe du joueur n°{i+1}: "
                )
                if player_sex in ['h', 'f']:
                    break
            player_ranking = int(
                self.view.tournament_data(
                    f"veuillez entrer le classement du joueur n°{i+1}: "
                )
            )
            player = Players(
                player_name, player_first_name,
                player_date_of_birth, player_sex,
                player_ranking
            )
            self.players.append(player)
            self.tournaments.list_players.append(player.player_table())

    def start_round(self):
        """retourne liste des joueur ranger par ordre des matchs dans un tours """
        while True:
            self.rounds.rounds_name = self.view.tournament_data(
                "veuillez entrer le nom du tour: "
            )
            if self.rounds.rounds_name in ["rounds1", "rounds2", "rounds3", "rounds4"]:
                break
        self.rounds.date_start_time = datetime.today().strftime('%d-%m-%Y %H:%M')
        if self.rounds.rounds_name == "rounds1":
            self.players = self.rounds.sort_by_rating(self.players)
            self.players = self.rounds.first_rounds(self.players)
        elif self.rounds.rounds_name in ["rounds2", "rounds3", "rounds4"]:
            self.players = self.rounds.sort_by_point(self.players)
            self.players = self.rounds.next_rounds(self.players)

    def end_rounds_results(self):
        """retourne le resultat de la tours """
        score = []
        players = []
        self.rounds.date_end_time = datetime.today().strftime('%d-%m-%Y %H:%M')
        for i in range(NUMBER_PLAYERS):
            score.append(float(
                    self.view.tournament_data(
                        f"veuillez entrer le score du {self.players[i].player_name}: "
                    )
                ))
            self.players[i].total_points += score[i]
            players.append(self.players[i].player_table())
        return self.rounds.rounds_results(players, score)

    def results(self):
        self.players = self.rounds.sort_by_point(self.players)
        tournaments_results = {}
        ranking = ['first:', 'second:', 'third:', 'fourth:', 'fifth:', 'sixth:', 'seventh:', 'eighth:']
        for i in range(NUMBER_PLAYERS):
            tournaments_results[ranking[i]] = self.players[i].player_table()
        self.tournaments.results = tournaments_results
        # print("classement des joueurs")
        # print(self.tournaments.results)
        self.view.show_results(tournaments_results)

        """print("classement des joueurs")
        for i in range(NUMBER_PLAYERS):
            print(f"-{i + 1}- {self.players[i].player_table()}\n"
                  f"avec un score de: {self.players[i].total_points}\n"
                  )"""

    def data_recovery(self, data):
        """data assignment retrieve"""
        self.tournaments.tournaments_name = data[0]['tournaments_name']
        self.tournaments.tournaments_venue = data[0]['tournaments_venue']
        self.tournaments.tournaments_date = data[0]['tournaments_date']
        self.tournaments.time_control = data[0]['time_control']
        self.tournaments.rounds_number = data[0]['rounds_number']
        self.tournaments.remarks_director = data[0]['remarks_director']
        self.tournaments.list_players = data[0]['list_players']
        self.tournaments.list_rounds_tournament = data[0]['list_rounds_tournament']
        self.tournaments.results = data[0]['results']
        print(self.tournaments)

    def continue_tournament(self):
        """data recovery from database"""
        tournament_data_base = TinyDB('data_base_tournaments.json')
        tournaments = self.view.tournament_data(
            "veuillez entrer le nom du tournoi à continuer: "
        )
        tournament_table = tournament_data_base.table('chess')  # f'{tournaments_name}'
        tournament = Query()
        data = tournament_table.search(tournament.tournaments_name == tournaments)
        self.data_recovery(data)

    def data_logging(self, element=''):
        """data storage"""
        if element == '':
            tournament_data_base = TinyDB('data_base_tournaments.json')
            tournament_table = tournament_data_base.table(f'{self.tournaments.tournaments_name}')
            tournament_table.insert(self.tournaments.tournaments_table())
        else:
            tournament_data_base = TinyDB('data_base_tournaments.json')
            tournament_table = tournament_data_base.table(f'{self.tournaments.tournaments_name}')
            list_rounds = self.tournaments.tournaments_table()
            tournament_table.update({element: list_rounds[element]})

    def run(self):
        """run the chess"""
        menu = self.view.show_menu()
        if menu == '1':
            self.get_tournaments()
            self.get_players()
            print(self.tournaments)
            element = ''
            while self.tournaments.rounds_number > 0:
                self.start_round()
                self.end_rounds_results()
                self.tournaments.list_rounds_tournament.append(self.rounds.rounds_table())
                self.data_logging(element)
                element = 'list_rounds_tournament'
                self.tournaments.rounds_number -= 1
            self.results()
            self.data_logging('results')
            self.data_logging('rounds_number')
        elif menu == '2':
            self.continue_tournament()
