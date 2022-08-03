from tinydb import TinyDB, Query, where


class Tournaments:

    def __init__(self, tournaments_name='',
                 tournaments_venue='',
                 tournaments_date=[], time_control="blitz",
                 remarks_director=[]
                 ):
        self.tournaments_name = tournaments_name
        self.tournaments_venue = tournaments_venue
        self.tournaments_date = tournaments_date
        self.time_control = time_control
        self.remarks_director = remarks_director
        self.list_rounds_tournament = {}

    def __str__(self):
        """Used in print."""
        return f"\nNom de la tournois:{self.tournaments_name}\n" \
               f"lieu de la tournois:{self.tournaments_venue}\n" \
               f"Date de la tournois:{self.tournaments_date}\n" \
               f"controle temps:{self.time_control}\n" \
               f"remarque du directeur:{self.remarks_director}\n"

    def __repr__(self):
        """Used in print."""
        return str(self)

    def tournaments_table(self):
        dict_tournaments = {
            'tournaments_name': self.tournaments_name,
            'tournaments_venue': self.tournaments_venue,
            'tournaments_date': self.tournaments_date,
            'remarks_director': self.remarks_director
        }
        return dict_tournaments

"""    def data_base_tournaments(self):
        data_base = TinyDB('data_base_tournaments.json')
        data_base.insert()"""
