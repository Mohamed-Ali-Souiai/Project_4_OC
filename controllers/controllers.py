"""Define the main controller."""

# from operator import attrgetter
from tinydb import TinyDB, Query
from datetime import datetime


from models.players import Player

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

    def control_score(self, player):
        while True:
            try:
                score = float(
                    self.view.tournament_data(
                        f"veuillez entrer le score du {self.players[player].player_name}: "
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
        print(self.tournaments)

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
        print(len(players_table))
        self.view.show_player(players_table)
        self.deserialized(players_table)

    def deserialized(self, table):
        if len(self.players) == 0:
            counter = 1
            for player in table:
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
        print('trie alphabetique')
        sort_players = sorted(self.players, key=lambda x: x.name)
        # self.players.sort(key=attrgetter('name'))
        self.view.show_player(sort_players)

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
        tournaments_results = {}
        ranking = ['first:', 'second:', 'third:', 'fourth:', 'fifth:', 'sixth:', 'seventh:', 'eighth:']
        for i in range(NUMBER_PLAYERS):
            tournaments_results[ranking[i]] = self.players[i].player_table()
        self.tournaments.results = tournaments_results
        self.view.show_results(tournaments_results)

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
        print(self.players)

    def continue_tournament(self):
        """data recovery from database"""
        tournament_data_base = TinyDB('data_base_tournaments.json')
        tournaments = self.view.tournament_data(
            "veuillez entrer le nom du tournoi à continuer: "
        )
        tournament_table = tournament_data_base.table(tournaments)  # f'{tournaments_name}'
        """tournament = Query()
        data = tournament_table.search(tournament.tournaments_name == tournaments)"""
        self.data_recovery(tournament_table)

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
        element = ''
        while self.tournaments.rounds_number > 0:
            self.generate_player_pairs()
            self.end_rounds_results()
            self.tournaments.list_rounds_tournament.append(self.rounds.rounds_table())
            self.data_logging(element)
            element = 'list_rounds_tournament'
            self.tournaments.rounds_number -= 1
            choice = self.view.tournament_data(
                "voulez vous continuer le tournoi: (y/n) "
            )
            if choice == 'n':
                break

    def run(self):
        """run the chess"""
        # boolean = True
        while True:
            menu = self.view.show_menu('principal')
            if menu == '1':

                sub_menu = self.view.show_menu()
                if sub_menu == '1':
                    self.import_player()
                elif sub_menu == '2':
                    self.get_players()
                self.get_tournaments()
                print(self.tournaments)
                self.start_rounds()
                self.results()
                self.data_logging('results')
                self.data_logging('rounds_number')
            elif menu == '2':
                self.continue_tournament()
                self.start_rounds()
                self.results()
                self.data_logging('results')
                self.data_logging('rounds_number')
            if menu == 4:
                break
