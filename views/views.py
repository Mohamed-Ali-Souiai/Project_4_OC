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
        for key in tournaments_results.keys():
            print(f'{key}:{tournaments_results[key]}')
        """self.players = self.rounds.sort_by_point(self.players)
        print("classement des joueurs")
        for i in range(NUMBER_PLAYERS):
            print(f"-{i + 1}- {self.players[i].player_table()}\n"
                  f"avec un score de: {self.players[i].total_points}\n"
                  )"""

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
                print("continuer une tournois")
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
