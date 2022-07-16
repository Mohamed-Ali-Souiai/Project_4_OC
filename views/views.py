class Views:
    def __init__(self):
        pass

    def show_players(self, players):
        print(players)

    def show_menu(self):
        pass

    def enter_tournaments_name(self):
        name = input("veuillez entrer le nom du tournois")
        if not name:
            return None
        return name

    def enter_tournaments_venue(self):
        venue = input("veuillez entrer le lieu du tournois")
        if not venue:
            return None
        return venue

    def enter_tournaments_date(self):
        date = input("veuillez entrer la date du tournois")
        if not date:
            return None
        return date

    def enter_tournaments_remarks_director(self):
        remarks_from_the_director = input("veuillez entrer la remarque  du derecteur")
        if not remarks_from_the_director:
            return None
        return remarks_from_the_director

    def enter_player_name(self):
        name = input("veuillez entrer le nom du joueur")
        if not name:
            return None
        return name

    def enter_player_first_name(self):
        first_name = input("veuillez entrer le prénom du joueur")
        if not first_name:
            return None
        return first_name

    def enter_player_date_of_birth(self):
        date_of_birth = input("veuillez entrer la date de naissance du joueur")
        if not date_of_birth:
            return None
        return date_of_birth

    def enter_player_sex(self):
        sex = input("veuillez entrer le sexe du joueur")
        if not sex:
            return None
        return sex

    def enter_player_ranking(self):
        ranking = input("veuillez entrer le classement du joueur")
        if not ranking:
            return None
        return ranking

    def get_score_first_player(self):
        first_player = input("veuillez saisir le score du premier joueur")
        return first_player

    def get_score_second_player(self):
        second_player = input("veuillez saisir le score du deuxieme joueur")
        return second_player
