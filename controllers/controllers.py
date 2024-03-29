"""Define the main controller."""

from tinydb import TinyDB, Query
from datetime import datetime
from models.player import Player

NUMBER_PLAYERS = 8
NUMBER_ROUNDS = 4


class Controllers:
    """Main controller."""

    def __init__(self, tournament, rounds, view, menu):
        self.players = []
        self.rounds = rounds
        self.view = view
        self.tournament = tournament
        self.menu = menu

    def control_date(self, date):
        """retourne une date valide"""
        try:
            datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            print('date non valide')
            return None
        return date

    def time_control(self):
        """retourne valeur valide"""
        while True:
            value = self.view.tournament_data(
                "veuillez choisir  le Controle du temps ('blitz','bullet','coup rapide'): "
            )
            if value in ['blitz', 'bullet', 'coup rapide']:
                break
            else:
                print('valeur non valide')
        return value

    def ranking_control(self):
        """retourne valeur valide"""
        while True:
            try:
                value = int(
                    self.view.tournament_data(
                        "veuillez entrer le classement du joueur: "
                    )
                )
                break
            except ValueError:
                print('valeur non valide')
        return value

    def tournament_name_control(self, list_tournament_names):
        """retourne valeur valide"""
        while True:
            value = self.view.tournament_data(
                "veuillez entrer le nom du tournoi à continuer: "
            )
            if value in list_tournament_names:
                break
            else:
                print('valeur non valide')
        return value

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
        self.tournament.time_control = self.time_control()
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
                    "veuillez entrer la date de naissance du joueur (jj-mm-aaaa): "
                )
                if self.control_date(player_date_of_birth):
                    break

            while condition:
                player_sex = self.view.tournament_data(
                    "veuillez entrer le sexe du joueur ('h','f'): "
                )
                if player_sex in ['h', 'f']:
                    break
            player_ranking = self.ranking_control()
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
        list_tournament_name = self.menu.import_tournament_names()
        self.view.show_system_message('liste des tournois enregistrés : ')
        for name in list_tournament_name:
            self.view.show_system_message(name)
        tournament_data_base = TinyDB('data_base_tournaments.json')
        tournament = self.tournament_name_control(list_tournament_name)
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
            if self.tournament.results:
                for key in self.tournament.results.keys():
                    name = self.tournament.results[key]['name']
                    first_name = self.tournament.results[key]['first_name']
                    date_of_birth = self.tournament.results[key][
                        'date_of_birth'
                    ]
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
            elif self.tournament.list_players:
                for i in range(len(self.tournament.list_players)):
                    name = self.tournament.list_players[i]['name']
                    first_name = self.tournament.list_players[i]['first_name']
                    date_of_birth = self.tournament.list_players[i][
                        'date_of_birth'
                    ]
                    sex = self.tournament.list_players[i]['sex']
                    ranking = self.tournament.list_players[i]['ranking']
                    total_points = self.tournament.list_players[i]['total_points']
                    opponent = self.tournament.list_players[i]['opponent']
                    player = Player(
                        name, first_name,
                        date_of_birth, sex,
                        ranking, total_points,
                        opponent
                    )
                    self.players.append(player)
            else:
                self.begin_tournament()

    def data_logging(self):
        """save tournament data '5' """
        tournament_data_base = TinyDB('data_base_tournaments.json')
        tournament_table = tournament_data_base.table('tournaments')
        tournament_table.update(self.tournament.tournament_table())

    def start_rounds(self):
        """start the rounds"""
        if self.tournament.rounds_number > 0:
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
            self.tournament.rounds_number -= 1
        else:
            self.view.show_system_message("les 4 rounds sont deja ete discute")

    def begin_tournament(self):
        """ start tournament '1' """
        sub_menu = self.view.show_menu()
        if sub_menu == '1':  # "Importer des joueurs"
            players_table = self.import_player()
            self.deserialized(players_table)
        elif sub_menu == '2':  # "Entrer des joueurs"
            self.get_players()
        if self.tournament.tournament_name == '':
            self.get_tournament()

    def run(self):
        """run the chess """
        while True:
            menu = self.view.show_menu('principal')
            if menu == '1':  # "Commencer un tournoi"
                choice = self.view.tournament_data('Vous etes sûr de vouloir commencer un tournoi (y/n)')
                if choice == 'y':
                    self.begin_tournament()
            elif menu == '2':  # "continuer un tournoi deja existante"
                choice = self.view.tournament_data(
                    'Vous etes sûrde vouloir continuer un tournoi deja existante (y/n)'
                )
                if choice == 'y':
                    self.continue_tournament()
            elif menu == '3':  # "jouer une round (rounds1, rounds2, rounds3, rounds4)"
                self.start_rounds()
                # self.results()
            elif menu == '4':  # "afficher les résultats"
                self.view.show_results(self.tournament.results)
            elif menu == '5':  # "sauvegader les donnes du tournoi"
                if self.tournament.rounds_number in [3, 2, 1, 0]:
                    self.menu.data_logging(self.tournament, self.tournament.tournament_name)
            elif menu == '6':  # "Liste de tous les joueurs du tournoi "
                self.menu.List_tournament_players(self.players)
            elif menu == '7':  # Liste de tous les joueurs dans la db
                self.menu.List_players_db()
            elif menu == '8':  # "Liste de tous les tournois"
                self.menu.List_all_tournaments()
            elif menu == '9':  # "Liste de tous les tours du tournoi"
                self.menu.List_tournament_rounds()
            elif menu == '10':  # "Liste de tous les matchs du tournoi"
                self.menu.List_tournament_matches()
            elif menu == '11':  # "modifier les classements"
                self.menu.search_player()
            else:
                break
