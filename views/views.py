"""Base view."""
from models.players import Player


class Views:
    def __init__(self):
        pass

    def tournament_data(self, message):
        """get data"""
        print()
        data = input(message)
        if not data:
            return None
        return data

    def show_results(self, tournaments_results):
        print("classement des joueurs")
        for key in tournaments_results.keys():
            print(f'{key}:{tournaments_results[key]}')

    def show_player(self, players):
        counter = 1
        for player in players:
            if counter == 1:
                print(f"{' ':3}|{'name':^15}|{'first_name':^15}|{'date_of_birth':^15} |{'sex':^15}|{'ranking':^15}|")
            print(f"{counter:<3}|{player['name']:15}|{player['first_name']:15}|"
                  f"{player['date_of_birth']:15} |{player['sex']:15}|"
                  f"{player['ranking']:<15}|")
            counter += 1

    def sow_tournament(self):
        pass

    def show_menu(self, show=''):

        if show == 'principal':
            menu = {'1': "Commencer un tournoi",
                    '2': "continuer un trournoi",
                    '3': "afficher les résultats",
                    '4': "Afficher les joueurs du tournoi"
                    }
            choice = ['1', '2', '3', '4']
        else:
            menu = {'1': "Afficher les joueurs enregistrés",
                    '2': "Entrer des joueurs",
                    '3': "Importer des joueurs",
                    '4': "Afficher les joueurs du tournoi"
                    }
            choice = ['1', '2', '3', '4']
        while True:
            print('****************menu****************')
            for key in menu.keys():
                print(f"{key}: {menu[key]}")
            select = input("Veuillez entrer la sélection:")
            if select in choice:
                print(f"votre chois est : {menu[select]}")
                return select
            else:
                print("chois invalide")
