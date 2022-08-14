"""Define the main controller."""

from operator import attrgetter
from tinydb import TinyDB, Query
from datetime import datetime
from models.players import Player
from pprint import pprint

NUMBER_PLAYERS = 8
NUMBER_ROUNDS = 4


class Controllers:
    """Main controller."""

    def __init__(self, tournaments, rounds, view):
        self.players = []
        self.rounds = rounds
        self.view = view
        self.tournaments = tournaments

    def control_date(self, date):
        """retourne une date valide"""
        try:
            datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            print('date non valide')
            return None
        return date

    def control_score(self, index):
        """retourne un valeur valide"""
        while True:
            try:
                score = float(
                    self.view.tournament_data(
                        f"veuillez entrer le score du {self.players[index].name}: "
                    )
                )
                break
            except ValueError:
                print('valeur non valide')
        return score

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
                f"veuillez entrer le nom du joueur : "
            )
            player_first_name = self.view.tournament_data(
                f"veuillez entrer le prénom du joueur : "
            )
            while condition:
                player_date_of_birth = self.view.tournament_data(
                    f"veuillez entrer la date de naissance du joueur : "
                )
                if self.control_date(player_date_of_birth):
                    break

            while condition:
                player_sex = self.view.tournament_data(
                    f"veuillez entrer le sexe du joueur : "
                )
                if player_sex in ['h', 'f']:
                    break
            player_ranking = int(
                self.view.tournament_data(
                    f"veuillez entrer le classement du joueur: "
                )
            )
            player = Player(
                player_name, player_first_name,
                player_date_of_birth, player_sex,
                player_ranking
            )
            self.players.append(player)
            self.tournaments.list_players.append(player.player_table())
            players_data_base = TinyDB('data_base_tournaments.json')
            players_table = players_data_base.table('players')
            players_table.insert(player.player_table())

    def import_player(self):
        players_data_base = TinyDB('data_base_tournaments.json')
        table = 'players'
        players_table = players_data_base.table(table)
        return players_table

    def deserialized(self, players):
        if len(self.players) == 0:
            counter = 1
            for player in players:
                name = player['name']
                first_name = player['first_name']
                date_of_birth = player['date_of_birth']
                sex = player['sex']
                ranking = player['ranking']
                total_points = player['total_points']
                opponent = player['opponent']
                player_information = Player(
                    name, first_name,
                    date_of_birth, sex,
                    ranking, total_points,
                    opponent
                )
                self.players.append(player_information)
                self.tournaments.list_players.append(player_information.player_table())
                counter += 1
                if counter == 9:
                    break

    def generate_player_pairs(self):
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
            score.append(self.control_score(i))
            self.players[i].total_points += score[i]
            players.append(self.players[i].player_table())
        return self.rounds.rounds_results(players, score)

    def results(self):
        self.players = self.rounds.sort_by_point(self.players)
        tournament_results = {}
        ranking = ['first:', 'second:', 'third:', 'fourth:', 'fifth:', 'sixth:', 'seventh:', 'eighth:']
        for i in range(NUMBER_PLAYERS):
            tournament_results[ranking[i]] = self.players[i].player_table()
        self.tournaments.results = tournament_results
        self.view.show_results(tournament_results)

    def continue_tournament(self):
        """data recovery from database"""
        tournament_data_base = TinyDB('data_base_tournaments.json')
        tournaments = self.view.tournament_data(
            "veuillez entrer le nom du tournoi à continuer: "
        )
        tournament_table = tournament_data_base.table(tournaments)
        request = Query()
        recovery = tournament_table.search(request.tournaments_name == tournaments)
        self.data_recovery(recovery)

    def data_recovery(self, data):
        """data assignment retrieve"""
        self.tournaments.tournaments_name = data[0]['tournaments_name']
        self.tournaments.tournaments_venue = data[0]['tournaments_venue']
        self.tournaments.tournaments_date.extend(data[0]['tournaments_date'])
        self.tournaments.time_control = data[0]['time_control']
        self.tournaments.rounds_number = data[0]['rounds_number']
        self.tournaments.remarks_director.extend(data[0]['remarks_director'])
        self.tournaments.list_players = data[0]['list_players']
        self.tournaments.list_rounds_tournament = data[0]['list_rounds_tournament']
        self.tournaments.results = data[0]['results']
        if len(self.players) == 0:
            for key in self.tournaments.results.keys():
                name = self.tournaments.results[key]['name']
                first_name = self.tournaments.results[key]['first_name']
                date_of_birth = self.tournaments.results[key]['date_of_birth']
                sex = self.tournaments.results[key]['sex']
                ranking = self.tournaments.results[key]['ranking']
                total_points = self.tournaments.results[key]['total_points']
                opponent = self.tournaments.results[key]['opponent']
                player = Player(
                    name, first_name,
                    date_of_birth, sex,
                    ranking, total_points,
                    opponent
                )
                self.players.append(player)

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

    def start_rounds(self):
        # while self.tournaments.rounds_number > 0:
        self.generate_player_pairs()
        """affiches paire"""
        self.view.show_system_message('*************** MATCH ***************')
        list_pair = self.rounds.list_pair(self.players)  # cette methode n'existe pas
        color = self.rounds.draw()
        self.view.show_match(list_pair, color)
        self.end_rounds_results()
        self.tournaments.list_rounds_tournament.append(self.rounds.rounds_table())
        """self.data_logging(element)
            element = 'list_rounds_tournament'
            self.tournaments.rounds_number -= 1
            choice = self.view.tournament_data(
                "voulez vous continuer le tournoi: (y/n) "
            )
            if choice == 'n':
                break
            else:
                self.view.show_system_message(
                    'le systeme va sauvegarder la progression'
                )
                self.data_logging()"""

    def run(self):
        """run the chess"""
        while True:
            menu = self.view.show_menu('principal')
            if menu == '1':  # "Commencer un tournoi"

                sub_menu = self.view.show_menu()
                if sub_menu == '1':  # "Importer des joueurs"
                    players_table = self.import_player()
                    self.deserialized(players_table)
                elif sub_menu == '2':  # "Entrer des joueurs"
                    self.get_players()
                else:  # "modifier les classements"
                    pass
                self.get_tournaments()
            elif menu == '2':  # "continuer un trournoi"
                self.continue_tournament()

            elif menu == '3':  # "jouer une round"
                self.start_rounds()
                self.tournaments.remarks_director.append(
                    self.view.tournament_data(
                        "veuillez entrer la remarque  du directeur: "
                    )
                )
            elif menu == '4':  # "afficher les résultats"
                self.results()
            elif menu == '5':  # "sauvegader les donnes du tournoi"
                if self.tournaments.rounds_number == 4:
                    self.data_logging()
                else:
                    self.data_logging('results')
                    self.data_logging('rounds_number')
            elif menu == '6':  # "Liste de tous les joueurs du tournoi "
                """players_table = self.import_player()
                self.deserialized(players_table)"""
                choice = self.view.tournament_data(
                    " 1 : par ordre alphabétique \n 2 : par classement) "
                )
                if choice in ['1', '2']:
                    if choice == '1':
                        sort_players = sorted(self.players, key=attrgetter('name'), reverse=False)
                        self.view.show_player(sort_players)
                    else:
                        sort_players = sorted(self.players, key=attrgetter('ranking'), reverse=False)
                        self.view.show_player(sort_players)
            elif menu == '7':  # "Liste de tous les joueurs dans la base de donnee "
                players_table = self.import_player()
                choice = self.view.tournament_data(
                    " 1 : par ordre alphabétique \n 2 : par classement) "
                )
                if choice in ['1', '2']:
                    if choice == '1':
                        sort_players = sorted(players_table, key=lambda value: value['name'], reverse=False)
                        self.view.show_player(sort_players)
                    else:
                        sort_players = sorted(players_table, key=lambda value: value['ranking'], reverse=False)
                        self.view.show_player(sort_players)
            elif menu == '8':  # "Liste de tous les tournois"
                pass
            elif menu == '9':  # "Liste de tous les tours du tournoi"
                pass
            elif menu == '10':  # "Liste de tous les matchs du tournoi"
                pass
            else:
                break
