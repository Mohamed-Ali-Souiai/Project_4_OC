from random import choice

class Match:

    def draw(self):
        """drawing of lot"""
        color_list = ['black', 'white']
        color = choice(color_list)
        return color

    def player_score(self, player, score):
        return [player, score]

    def player_pair(self, first_player, second_player):
        return first_player, second_player
