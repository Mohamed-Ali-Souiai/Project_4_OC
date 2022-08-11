from views.views import Views
from controllers.controllers import Controllers
from models.tournaments import Tournaments
from models.rounds import Rounds



def main():
    views = Views()
    rounds = Rounds()
    tournaments = Tournaments()
    chess_tournaments = Controllers(tournaments, rounds, views)
    chess_tournaments.run()


if __name__ == '__main__':
    main()

