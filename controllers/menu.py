"""controllers menu."""

from tinydb import TinyDB, Query
from operator import attrgetter

from views.views import Views


class Menu:

    def __init__(self):
        self.view = Views()

    def import_player(self):
        """returns the player table"""
        players_data_base = TinyDB('data_base_tournaments.json')
        table = 'players'
        players_table = players_data_base.table(table)
        return players_table

    def table_all_tournaments(self):
        """returns the tournament table """
        tournament_data_base = TinyDB('data_base_tournaments.json')
        tournament_table = tournament_data_base.table('tournaments')
        return tournament_table

    def data_logging(self, tournament, name):
        """save tournament data '5' """
        tournament_data_base = TinyDB('data_base_tournaments.json')
        tournament_table = tournament_data_base.table('tournaments')
        target = Query()
        tournament_table.update(tournament.tournament_table(), target.tournament_name == name)

    def List_tournament_players(self, players):
        """List of all tournament players '6' """
        choice = self.view.tournament_data(
            " 1 : par ordre alphabétique \n 2 : par classement) "
        )
        if choice in ['1', '2']:
            if choice == '1':
                sort_players = sorted(
                    players, key=attrgetter('name'), reverse=False
                )
                self.view.show_player(sort_players)
            else:
                sort_players = sorted(
                    players, key=attrgetter('ranking'),
                    reverse=False
                )
                self.view.show_player(sort_players)

    def List_players_db(self):
        """ List of all players in the database '7' """
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

    def List_all_tournaments(self):
        """List of all tournaments '8' """
        tournament_table = self.table_all_tournaments()
        self.view.sow_tournament(tournament_table)

    def List_tournament_rounds(self):
        """List of all tournament rounds '9' """
        table = self.table_all_tournaments()
        query = Query()
        name = self.view.tournament_data(
            "veuillez entrer le nom de tournois"
        )
        tournament = table.search(
            query.tournament_name == name
        )
        self.view.show_rounds(tournament)

    def List_tournament_matches(self):
        """List of all tournament matches '10' """
        table = self.table_all_tournaments()
        query = Query()
        name = self.view.tournament_data(
            "veuillez entrer le nom de tournois"
        )
        tournament = table.search(
            query.tournament_name == name
        )
        self.view.show_match(tournament)

    def search_player(self):
        """search for player to update them '11' """
        players_data_base = TinyDB('data_base_tournaments.json')
        table = players_data_base.table('players')
        query = Query()
        name = self.view.tournament_data(
            "veuillez entrer le nom du joueur :"
        )
        value = int(self.view.tournament_data(
            "veuillez entrer le nouveau valeur :"
        ))
        table.update({'ranking': value}, query.name == name)
