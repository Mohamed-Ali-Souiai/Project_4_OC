from tinydb import TinyDB, Query


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

    def tournaments_table(self):
        tournaments = {
            'tournaments_name': self.tournaments_name,
            'tournaments_venue': self.tournaments_venue,
            'tournaments_date': self.tournaments_date,
            'remarks_director': self.remarks_director
        }

    def data_base_tournaments(self, insert):
        data_base = TinyDB('data_base_tournaments.json')
        data_base.insert(self.list_rounds_tournament)
