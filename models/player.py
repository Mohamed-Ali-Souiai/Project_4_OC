
class Player:
    def __init__(self, name, first_name,
                 date_of_birth, sex,
                 ranking, points=0,
                 opponent=[]
                 ):
        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.ranking = ranking
        self.total_points = points
        self.opponent = opponent

    def __str__(self):
        """Used in print."""
        return (
            f"\nNom de famille: {self.name}\n"
            f"Prénom: {self.first_name}\n"
            f"Date de naissance: {self.date_of_birth}\n"
            f"Sexe: {self.sex}\n"
            f"Classement: {self.ranking}\n"
        )

    def __repr__(self):
        """Used in print."""
        return str(self)

    def __getitem__(self, item):
        """Used in print."""
        return self.__dict__[item]

    def player_table(self):
        """serialize the player instance"""
        serialized = {
            'name': self.name,
            'first_name': self.first_name,
            'date_of_birth': self.date_of_birth,
            'sex': self.sex,
            'ranking': self.ranking,
            'total_points': self.total_points,
            'opponent': self.opponent
        }
        return serialized
    