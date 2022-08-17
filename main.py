"""Entry point."""

from views.views import Views
from controllers.controllers import Controllers
from controllers.menu import Menu
from models.tournament import Tournament
from models.rounds import Rounds


def main():
    views = Views()
    rounds = Rounds()
    tournament = Tournament()
    menu = Menu()
    chess_tournament = Controllers(tournament, rounds, views, menu)
    chess_tournament.run()


if __name__ == '__main__':
    main()
