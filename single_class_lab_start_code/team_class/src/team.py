class Team:
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0

    def add_player(self, player):
        self.players.append(player)

    def has_player(self, to_find):
        found = False
        for player in self.players:
            if player == to_find:
                found = True
        return found
# could also just return self.players.count(player) > 0
# return player in self.players another soloution will only return true or false 


    def play_game(self, game_result):
        if game_result == True:
            self.points += 3