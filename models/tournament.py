"""Tournament."""

NUMBER_OF_ROUND = 4


class Tournament:

    def __init__(self, tournament_name='',
                 tournament_venue='',
                 tournament_date=[], time_control="blitz",
                 remarks_director=[]
                 ):
        self.tournament_name = tournament_name
        self.tournament_venue = tournament_venue
        self.tournament_date = tournament_date
        self.rounds_number = NUMBER_OF_ROUND
        self.time_control = time_control
        self.remarks_director = remarks_director
        self.list_players = []
        self.list_rounds_tournament = []  # ********
        self.results = {}

    def __str__(self):
        """Used in print."""
        return (
            f"\nNom de la tournois:{self.tournament_name}\n"
            f"lieu de la tournois:{self.tournament_venue}\n"
            f"Date de la tournois:{self.tournament_date}\n"
            f"nombre des tours:{self.rounds_number}\n"
            f"controle temps:{self.time_control}\n"
            f"remarque du directeur:{self.remarks_director}\n"
            f"liste des joueurs:{self.list_players}\n"
            f"list_rounds_tournament:{self.list_rounds_tournament}\n"
            f"resultat:{self.results}"
        )

    def __repr__(self):
        """Used in print."""
        return str(self)

    def __getitem__(self, item):
        """Used in print."""
        return self.__dict__[item]

    def tournament_table(self):
        """serialize the tournament instance"""
        dict_tournament = {
            'tournament_name': self.tournament_name,
            'tournament_venue': self.tournament_venue,
            'tournament_date': self.tournament_date,
            'rounds_number': self.rounds_number,
            'time_control': self.time_control,
            'remarks_director': self.remarks_director,
            'list_players': self.list_players,
            'list_rounds_tournament': self.list_rounds_tournament,
            'results': self.results
        }
        return dict_tournament
