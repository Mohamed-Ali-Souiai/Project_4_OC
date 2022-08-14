#!C:\Users\mohamed ali\Desktop\git\Project_4_OC\env python
# -*- coding: utf-8 -*-

"""Base view."""


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
        print("classement des joueurs dans le tournoi")
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

    def show_match(self, players, colors):
        counter = 1
        for player_pair,color_pair in zip(players,colors):
            if counter == 1:
                print(f"{'name':^15}|{'first_name':^15}|{'ranking':^15}|{'color':^15}|")
            print(f'**********  match N°{counter}  **********')
            for player,color in zip(player_pair,color_pair):
                print(f"{player['name']:15}|{player['first_name']:15}|"
                      f"{player['ranking']:<15}|{color['ranking']:<15}|")
            counter += 1


    def sow_tournament(self):
        pass

    def show_system_message(self, message):
        print(message)

    def show_menu(self, show=''):

        if show == 'principal':
            menu = {
                '1': "Commencer un tournoi",
                '2': "continuer un trournoi",
                '3': "jouer une round",
                '4': "afficher les résultats",
                '5': "sauvegader les donnes du tournoi",
                '6': "Liste de tous les joueurs du tournoi ",
                '7': "Liste de tous les joueurs dans la base de donnee ",
                '8': "Liste de tous les tournois",
                '9': "Liste de tous les tours du tournoi",
                '10': "Liste de tous les matchs du tournoi",
                '0': "quitter"
            }
            choice = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        else:
            menu = {
                '1': "Importer des joueurs",
                '2': "Entrer des joueurs",
                '3': "modifier les classements"
            }
            choice = ['1', '2']
        while True:
            print('*************** menu ***************')
            for key in menu.keys():
                print(f"{key:^3}: {menu[key]:50}")
            select = input("Veuillez entrer la sélection:")
            if select in choice:
                print(f"votre chois est : {menu[select]}")
                return select
            else:
                print("chois invalide")
