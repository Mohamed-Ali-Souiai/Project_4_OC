#!C:\Users\mohamed ali\Desktop\git\Project_4_OC\env python
# -*- coding: utf-8 -*-

"""Define the main view. """

NUMBER_PLAYERS = 8
ROUNDS_NUMBER = 4


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

    def show_results(self, tournament_results):
        """display list the result"""
        print("classement des joueurs dans le tournoi")
        for key in tournament_results.keys():
            print(f"{key:9} {tournament_results[key]['name']:10} "
                  f"{tournament_results[key]['first_name']:10}"
                  f"avec score de '{tournament_results[key]['total_points']:10}'")

    def show_player(self, players):
        """player list poster"""
        counter = 1
        for player in players:
            if counter == 1:
                print(f"{' ':3}|{'name':^15}|{'first_name':^15}|"
                      f"{'date_of_birth':^15}|{'sex':^15}|{'ranking':^15}|")
            print(f"{counter:3}|{player['name']:15}|{player['first_name']:15}|"
                  f"{player['date_of_birth']:15} |{player['sex']:15}|"
                  f"{player['ranking']:<15}|")
            counter += 1

    def show_meetings(self, players, colors):
        """displays the list of matches"""
        counter = 1
        for player_pair, color_pair in zip(players, colors):
            if counter == 1:
                print(f"{'name':^15}|{'first_name':^15}|"
                      f"{'ranking':^15}|{'color':^15}|")
            print(f'**********  match N°{counter}  **********')
            for player, color in zip(player_pair, color_pair):
                print(f"{player['name']:15}|{player['first_name']:15}|"
                      f"{player['ranking']:<15}|{color:<15}|")
            counter += 1

    def show_match(self, tournament):
        for i in range(ROUNDS_NUMBER):
            list_rounds = tournament[0]['list_rounds_tournament']
            print(f"************************* rounds{i+1} *************************")
            for match in list_rounds[i]['list_match']:
                print(f"{match[0][0]['name']:10} {match[0][0]['first_name']:10} : {match[0][1]}   VS   "
                      f"{match[1][0]['name']:10} {match[1][0]['first_name']:10} : {match[1][1]}")

    def show_rounds(self, tournament):
        for i in range(ROUNDS_NUMBER):
            list_rounds = tournament[0]['list_rounds_tournament']
            print(f" {list_rounds[i]['rounds_name']:^30}")
            print(f"date debut       :{list_rounds[i]['date_start_time']}")
            print(f"date fin         :{list_rounds[i]['date_end_time']}")
            print("resultats         :")
            for key in list_rounds[i]['results'].keys():
                print(f"{key:9} {list_rounds[i]['results'][key]['name']:10} "
                      f"{list_rounds[i]['results'][key]['first_name']:10}"
                      f"avec score de '{list_rounds[i]['results'][key]['total_points']:10}'")

    def sow_tournament(self, table):
        """displays the list of tournaments"""
        counter = 1
        for tournament in table:
            if counter == 1:
                print(f"-*- nom du tournoi        : {tournament['tournament_name']}\n"
                      f"-*- lieu du tournoi       : {tournament['tournament_venue']}\n"
                      f"-*- Date du tournoi       : {tournament['tournament_date']}\n"
                      f"-*- controle du temps     : {tournament['time_control']}\n"
                      f"-*- remarque du directeur :")
                for remark in tournament['remarks_director']:
                    print(f"    - {remark}")
                print('-*-resultats:')
                for key in tournament['results'].keys():
                    print(f"{key:9} {tournament['results'][key]['name']:10} "
                          f"{tournament['results'][key]['first_name']:10}"
                          f"avec score de '{tournament['results'][key]['total_points']:10}'")

    def show_system_message(self, message):
        """displays a system message"""
        print(message)

    def show_menu(self, show=''):
        """returns the choice select"""
        if show == 'principal':
            menu = {
                '1': "Commencer un tournoi",
                '2': "continuer un tournoi deja existante",
                '3': "jouer une round (rounds1, rounds2, rounds3, rounds4)",
                '4': "afficher les résultats",
                '5': "sauvegader les donnes du tournoi",
                '6': "Liste de tous les joueurs du tournoi ",
                '7': "Liste de tous les joueurs dans la base de donnee ",
                '8': "Liste de tous les tournois",
                '9': "Liste de tous les tours du tournoi",
                '10': "Liste de tous les matchs du tournoi",
                '11': "modifier les classements",
                '0': "quitter"
            }
            choice = [
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'
            ]
        else:
            menu = {
                '1': "Importer des joueurs",
                '2': "Entrer des joueurs"
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
