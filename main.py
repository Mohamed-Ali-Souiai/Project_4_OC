from views.views import Views
from controllers.controllers import Controllers
from models.rounds import Rounds


def main():
    views = Views()
    rounds = Rounds()
    chess = Controllers(rounds, views)
    chess.run()


if __name__ == '__main__':
    main()
