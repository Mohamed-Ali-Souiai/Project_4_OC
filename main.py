from views.views import Views
from controllers.controllers import Controllers
from models.rounds import Rounds


def main():
    views = Views()
    rounds = Rounds()
    chess_tournaments = Controllers(rounds, views)
    chess_tournaments.start_tournament()


if __name__ == '__main__':
    main()
