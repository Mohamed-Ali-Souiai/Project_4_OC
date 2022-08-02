
class Players:
    def __init__(self, player_name, player_first_name,
                 player_date_of_birth, player_sex,
                 player_ranking, total_points=0
                 ):
        self.player_name = player_name
        self.player_first_name = player_first_name
        self.player_date_of_birth = player_date_of_birth
        self.player_sex = player_sex
        self.player_ranking = player_ranking
        self.opponent_player = []
        self.total_points = total_points

    def player_table(self):
        player = {
            'name': self.player_name,
            'first_name': self.player_first_name,
            'player_date_of_birth': self.player_date_of_birth,
            'player_sex': self.player_sex,
            'player_ranking': self.player_ranking,
            'total_points': self.total_points
        }

