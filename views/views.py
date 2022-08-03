class Views:
    def __init__(self):
        pass

    def show_players(self, players):
        for i in range(len(players)):
            print(players[i].player_name)
            print(players[i].player_first_name)
            print(players[i].player_date_of_birth)
            print(players[i].player_sex)
            print(players[i].player_ranking)

    def show_details_tournament(self, tournament):
        print(tournament.tournaments_name)
        print(tournament.tournaments_venue)
        print(tournament.tournaments_date)
        print(tournament.time_control)
        print(tournament.remarks_director)

    def tournament_data(self, message):
        print()
        data = input(message)
        if not data:
            return None
        return data

    def show_menu(self):
        global selection
        menu = {'1': "Commencer un tournoi",
                '2': "modifier le classement des joueurs",
                '3': "afficher les résultats",
                '4': "quitter"
                }
        select = False
        while not select:
            options = menu.keys()
            options = sorted(options)
            for entry in options:
                print(entry, menu[entry])
            selection = input("Veuillez entrer la sélection: ")
            if selection == '1':
                print("Commencer un tournoi")
                select = True
            elif selection == '2':
                print("modifier le classement des joueurs")
                select = True
            elif selection == '3':
                print("afficher les résultats")
                select = True
            elif selection == '4':
                print("quitter")
                select = True
            else:
                print("Option sélectionnée inconnue !")
        if selection in ['1', '2', '3', '4']:
            return selection
        else:
            return None



