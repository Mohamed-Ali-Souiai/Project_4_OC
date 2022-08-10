NUMBER_OF_ROUND = 4


class Tournaments:

    def __init__(self, tournaments_name='',
                 tournaments_venue='',
                 tournaments_date=[], time_control="blitz",
                 remarks_director=[]
                 ):
        self.tournaments_name = tournaments_name
        self.tournaments_venue = tournaments_venue
        self.tournaments_date = tournaments_date
        self.rounds_number = NUMBER_OF_ROUND
        self.time_control = time_control
        self.remarks_director = remarks_director
        self.list_players = []
        self.list_rounds_tournament = []  # ********
        self.results = {}

    def __str__(self):
        """Used in print."""
        return f"\nNom de la tournois:{self.tournaments_name}\n" \
               f"lieu de la tournois:{self.tournaments_venue}\n" \
               f"Date de la tournois:{self.tournaments_date}\n" \
               f"nombre des tours:{self.rounds_number}\n" \
               f"controle temps:{self.time_control}\n" \
               f"remarque du directeur:{self.remarks_director}\n" \
               f"liste des joueurs:{self.list_players}\n" \
               f"list_rounds_tournament:{self.list_rounds_tournament}\n" \
               f"resultat:{self.results}"

    def __repr__(self):
        """Used in print."""
        return str(self)

    def tournaments_table(self):
        dict_tournaments = {
            'tournaments_name': self.tournaments_name,
            'tournaments_venue': self.tournaments_venue,
            'tournaments_date': self.tournaments_date,
            'rounds_number': self.rounds_number,
            'time_control': self.time_control,
            'remarks_director': self.remarks_director,
            'list_players': self.list_players,
            'list_rounds_tournament': self.list_rounds_tournament,
            'results': self.results
        }
        return dict_tournaments
