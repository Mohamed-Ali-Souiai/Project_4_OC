from views.views import Views
from controllers.controllers import Controllers
from models.rounds import Rounds
from models.tournaments import Tournaments


def main():
    views = Views()
    # tournaments = Tournaments()
    rounds = Rounds()
    chess = Controllers(rounds, views)
    chess.run()


if __name__ == '__main__':
    main()

