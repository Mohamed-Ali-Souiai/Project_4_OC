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

    def show_menu(self):
        pass

    def tournament_data(self, message):
        data = input(message)
        if not data:
            return None
        return data
