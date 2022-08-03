
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

    def __str__(self):
        """Used in print."""
        return f"\nNom de famille:{self.player_name}\n" \
               f"Prénom:{self.player_first_name}\n" \
               f"Date de naissance:{self.player_date_of_birth}\n" \
               f"Sexe:{self.player_sex}\n" \
               f"Classement:{self.player_ranking}\n"

    def __repr__(self):
        """Used in print."""
        return str(self)

    def player_table(self):
        dict_player = {
            'name': self.player_name,
            'first_name': self.player_first_name,
            'player_date_of_birth': self.player_date_of_birth,
            'player_sex': self.player_sex,
            'player_ranking': self.player_ranking,
            'total_points': self.total_points
        }
        return dict_player

