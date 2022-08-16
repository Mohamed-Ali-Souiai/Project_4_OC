from views.views import Views
from controllers.controllers import Controllers
from models.tournament import Tournament
from models.rounds import Rounds


def main():
    views = Views()
    rounds = Rounds()
    tournament = Tournament()
    chess_tournament = Controllers(tournament, rounds, views)
    chess_tournament.run()


if __name__ == '__main__':
    main()
