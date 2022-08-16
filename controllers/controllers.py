"""Define the main controller."""

from operator import attrgetter
from tinydb import TinyDB, Query
from datetime import datetime
from models.player import Player

NUMBER_PLAYERS = 8
NUMBER_ROUNDS = 4


class Controllers:
    """Main controller."""

    def __init__(self, tournament, rounds, view):
        self.players = []
        self.rounds = rounds
        self.view = view
        self.tournament = tournament

    def control_date(self, date):
        """retourne une date valide"""
        try:
            datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            print('date non valide')
            return None
        return date

    def control_score(self, index):
        """returns a valid value"""
        while True:
            try:
                score = float(
                    self.view.tournament_data(
                        f"veuillez entrer le score du "
                        f"{self.players[index].name}: "
                    )
                )
                break
            except ValueError:
                print('valeur non valide')
        return score

    def get_tournament(self):
        """returns tournament details"""
        self.tournament.tournament_name = self.view.tournament_data(
            "veuillez entrer le nom du tournois: "
        )
        self.tournament.tournament_venue = self.view.tournament_data(
            "veuillez entrer le lieu du tournois: "
        )
        self.tournament.tournament_date.append(
            datetime.today().strftime('%d-%m-%Y')
        )
        self.tournament.time_control = self.view.tournament_data(
            "veuillez entrer le Controle du temps: "
        )
        self.tournament.remarks_director.append(
            self.view.tournament_data(
                "veuillez entrer la remarque  du directeur: "
            )
        )
        tournament_data_base = TinyDB('data_base_tournaments.json')
        tournament_table = tournament_data_base.table('tournaments')
        tournament_table.insert(self.tournament.tournament_table())

    def get_players(self):
        """returns the list of players"""
        condition = True
        for i in range(NUMBER_PLAYERS):
            print()
            player_name = self.view.tournament_data(
                "veuillez entrer le nom du joueur : "
            )
            player_first_name = self.view.tournament_data(
                "veuillez entrer le prénom du joueur : "
            )
            while condition:
                player_date_of_birth = self.view.tournament_data(
                    "veuillez entrer la date de naissance du joueur : "
                )
                if self.control_date(player_date_of_birth):
                    break

            while condition:
                player_sex = self.view.tournament_data(
                    "veuillez entrer le sexe du joueur : "
                )
                if player_sex in ['h', 'f']:
                    break
            player_ranking = int(
                self.view.tournament_data(
                    "veuillez entrer le classement du joueur: "
                )
            )
            player = Player(
                player_name, player_first_name,
                player_date_of_birth, player_sex,
                player_ranking
            )
            self.players.append(player)
            self.tournament.list_players.append(player.player_table())
            players_data_base = TinyDB('data_base_tournaments.json')
            players_table = players_data_base.table('players')
            players_table.insert(player.player_table())

    def import_player(self):
        """returns the player table"""
        players_data_base = TinyDB('data_base_tournaments.json')
        table = 'players'
        players_table = players_data_base.table(table)
        return players_table

    def deserialized(self, players):
        """deserialize player instances"""
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
                self.tournament.list_players.append(
                    player_information.player_table()
                )
                counter += 1
                if counter == 9:
                    break

    def generate_player_pairs(self):
        """returns list of players sorted by order of matches in a round"""
        while True:
            self.rounds.rounds_name = self.view.tournament_data(
                "veuillez entrer le nom du tour: "
            )
            if self.rounds.rounds_name in [
                "rounds1", "rounds2", "rounds3", "rounds4"
            ]:
                break
        self.rounds.date_start_time = datetime.today().strftime(
            '%d-%m-%Y %H:%M'
        )
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
        """generates the results"""
        self.players = self.rounds.sort_by_point(self.players)
        tournament_results = {}
        ranking = [
            'first:', 'second:', 'third:', 'fourth:',
            'fifth:', 'sixth:', 'seventh:', 'eighth:'
        ]
        for i in range(NUMBER_PLAYERS):
            tournament_results[ranking[i]] = self.players[i].player_table()
        self.rounds.results = tournament_results.copy()
        self.tournament.results = tournament_results

    def continue_tournament(self):
        """data recovery from database"""
        tournament_data_base = TinyDB('data_base_tournaments.json')
        tournament = self.view.tournament_data(
            "veuillez entrer le nom du tournoi à continuer: "
        )
        tournament_table = tournament_data_base.table('tournaments')
        request = Query()
        recovery = tournament_table.search(
            request.tournament_name == tournament
        )
        self.data_recovery(recovery)

    def data_recovery(self, data):
        """data assignment retrieve"""
        self.tournament.tournament_name = data[0]['tournament_name']
        self.tournament.tournament_venue = data[0]['tournament_venue']
        self.tournament.tournament_date.extend(data[0]['tournament_date'])
        self.tournament.time_control = data[0]['time_control']
        self.tournament.rounds_number = data[0]['rounds_number']
        self.tournament.remarks_director.extend(data[0]['remarks_director'])
        self.tournament.list_players = data[0]['list_players']
        self.tournament.list_rounds_tournament = data[0][
            'list_rounds_tournament'
        ]
        self.tournament.results = data[0]['results']
        if len(self.players) == 0:
            for key in self.tournament.results.keys():
                name = self.tournament.results[key]['name']
                first_name = self.tournament.results[key]['first_name']
                date_of_birth = self.tournament.results[key]['date_of_birth']
                sex = self.tournament.results[key]['sex']
                ranking = self.tournament.results[key]['ranking']
                total_points = self.tournament.results[key]['total_points']
                opponent = self.tournament.results[key]['opponent']
                player = Player(
                    name, first_name,
                    date_of_birth, sex,
                    ranking, total_points,
                    opponent
                )
                self.players.append(player)

    def data_logging(self):
        """data storage"""
        tournament_data_base = TinyDB('data_base_tournaments.json')
        tournament_table = tournament_data_base.table('tournaments')
        tournament_table.update(self.tournament.tournament_table())

    def start_rounds(self):
        """start the rounds"""
        self.generate_player_pairs()
        """affiches paire"""
        self.view.show_system_message('*************** MATCH ***************')
        list_pair = self.rounds.list_pair(self.players)
        color = self.rounds.draw()
        self.view.show_meetings(list_pair, color)
        self.end_rounds_results()
        self.results()
        self.tournament.list_rounds_tournament.append(
            self.rounds.rounds_table()
        )
        self.tournament.remarks_director.append(
            self.view.tournament_data(
                "veuillez entrer la remarque  du directeur: "
            )
        )
        if self.rounds.rounds_name == 'rounds2':
            self.tournament.rounds_number = 3
        elif self.rounds.rounds_name == 'rounds3':
            self.tournament.rounds_number = 2
        elif self.rounds.rounds_name == 'rounds4':
            self.tournament.rounds_number = 1

    def table_all_tournaments(self):
        """returns the tournament table"""
        tournament_data_base = TinyDB('data_base_tournaments.json')
        tournament_table = tournament_data_base.table('tournaments')
        return tournament_table

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
                self.get_tournament()
            elif menu == '2':  # "continuer un trournoi"
                self.continue_tournament()

            elif menu == '3':  # "jouer une round"
                self.start_rounds()
                # self.results()
            elif menu == '4':  # "afficher les résultats"
                self.view.show_results(self.tournament.results)
            elif menu == '5':  # "sauvegader les donnes du tournoi"
                if self.tournament.rounds_number in [4, 3, 2, 1]:
                    self.data_logging()
            elif menu == '6':  # "Liste de tous les joueurs du tournoi "
                choice = self.view.tournament_data(
                    " 1 : par ordre alphabétique \n 2 : par classement) "
                )
                if choice in ['1', '2']:
                    if choice == '1':
                        sort_players = sorted(
                            self.players, key=attrgetter('name'), reverse=False
                        )
                        self.view.show_player(sort_players)
                    else:
                        sort_players = sorted(
                            self.players, key=attrgetter('ranking'),
                            reverse=False
                        )
                        self.view.show_player(sort_players)
            elif menu == '7':  # Liste de tous les joueurs dans la db
                players_table = self.import_player()
                choice = self.view.tournament_data(
                    " 1 : par ordre alphabétique \n 2 : par classement) "
                )
                if choice in ['1', '2']:
                    if choice == '1':
                        sort_players = sorted(
                            players_table, key=lambda value: value['name'],
                            reverse=False
                        )
                        self.view.show_player(sort_players)
                    else:
                        sort_players = sorted(
                            players_table, key=lambda value: value['ranking'],
                            reverse=False
                        )
                        self.view.show_player(sort_players)
            elif menu == '8':  # "Liste de tous les tournois"
                tournament_table = self.table_all_tournaments()
                self.view.sow_tournament(tournament_table)
            elif menu == '9':  # "Liste de tous les tours du tournoi"
                table = self.table_all_tournaments()
                query = Query()
                name = self.view.tournament_data(
                    "veuillez entrer le nom de tournois"
                )
                tournament = table.search(
                    query.tournament_name == name
                )
                self.view.show_rounds(tournament)
            elif menu == '10':  # "Liste de tous les matchs du tournoi"
                table = self.table_all_tournaments()
                query = Query()
                name = self.view.tournament_data(
                    "veuillez entrer le nom de tournois"
                )
                tournament = table.search(
                    query.tournament_name == name
                )
                self.view.show_match(tournament)
            elif menu == '11':  # "modifier les classements"
                players_data_base = TinyDB('data_base_tournaments.json')
                table = players_data_base.table('players')
                query = Query()
                name = self.view.tournament_data(
                    "veuillez entrer le nom du joueur"
                )
                player = table.search(query.name == name)
            else:
                break
