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

    def control_date(self, date):
        try:
            datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            print('date non valide')
            return None
        return date

    def get_tournaments(self):
        date = []
        remarks_director = []
        name = self.view.tournament_data(
            "veuillez entrer le nom du tournois"
        )
        venue = self.view.tournament_data(
            "veuillez entrer le lieu du tournois"
        )
        date.append(datetime.today().strftime('%d-%m-%Y'))
        time_control = self.view.tournament_data(
            "veuillez entrer le Controle du temps"
        )
        remarks_director.append(
            self.view.tournament_data(
                "veuillez entrer la remarque  du derecteur"
            )
        )
        self.tournament_details = Tournaments(
            name, venue,
            date, time_control,
            remarks_director
        )

    def get_players(self):
        condition = True
        for i in range(NUMBER_OF_PLAYERS):
            # while len(self.players) < 9:
            print()
            player_name = self.view.tournament_data(
                "veuillez entrer le nom du joueur"
            )
            player_first_name = self.view.tournament_data(
                "veuillez entrer le prénom du joueur"
            )
            while condition:
                player_date_of_birth = self.view.tournament_data(
                    "veuillez entrer la date de naissance du joueur"
                )
                if self.control_date(player_date_of_birth):
                    break

            while condition:
                player_sex = self.view.tournament_data(
                    "veuillez entrer le sexe du joueur"
                )
                if player_sex in ['h', 'f']:
                    break
            player_ranking = int(
                self.view.tournament_data(
                    "veuillez entrer le classement du joueur"
                )
            )
            player = Players(
                player_name, player_first_name,
                player_date_of_birth, player_sex,
                player_ranking
            )
            self.players.append(player)

    """def single_match(self, player, score):
        match = Match(player, score)
        match.player_score()"""

    def rounds_results(self):
        self.rounds.end_date_time = datetime.today().strftime('%d-%m-%Y %H:%M')
        for i in range(NUMBER_OF_PLAYERS):
            self.players[i].player_score += float(
                    self.view.tournament_data(
                        f"veuillez entrer le score du {self.players[i].player_name}"
                    )
                )

    def show_results(self):
        pass

    def start_round(self,):
        """retourne liste des match """
        while True:
            self.rounds.rounds_name = self.view.tournament_data(
                "veuillez entrer le nom du tour"
            )
            if self.rounds.rounds_name in ["rounds1", "rounds2", "rounds3", "rounds4"]:
                break
        self.rounds.date_start_time = datetime.today().strftime('%d-%m-%Y %H:%M')
        if self.rounds.rounds_name == "rounds1":
            self.players = self.rounds.sort_by_rating(self.players)
            list_match = self.rounds.first_rounds(self.players)
            return list_match
        elif self.rounds.rounds_name in ["rounds2", "rounds3", "rounds4"]:
            self.players = self.rounds.sort_by_point(self.players)
            for player in self.players:
                print(vars(player))
            self.players = self.rounds.next_rounds(self.players)

    def start_tournament(self):
        menu = self.view.show_menu()
        if menu == '1':
            self.get_tournaments()
            self.get_players()
        elif menu == '2':
            self.start_round()
        elif menu == '3':
            self.rounds_results()
        elif menu == '4':
            self.show_results()
        list_match = self.start_round()
        print(f'\n le tournois : {vars(self.tournament_details)} \n')
        print(f'liste des matchs du tour{vars(self.rounds)}')
        for match in list_match:
            print(vars(match))
        self.rounds_results()
        self.start_round()
        print(f'\n le tournois : {vars(self.tournament_details)}')

        print(f'\n liste des matchs du tour{vars(self.rounds)}')
        for player in self.players:
            print(vars(player))

        # self.players = self.rounds.sort_by_rating(self.players)
        # self.view.show_details_tournament(tournament)
        # self.view.show_players(self.players)
