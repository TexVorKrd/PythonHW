import candy


class Game_list():
    def __init__(self):
        self.games = {}

    def add_game(self,id_player: str, name: str):
        if id_player not in self.games.keys():
            self.games[id_player] = candy.Candy(name)
        return self.games.get(id_player)

    def get_game(self,id_player: str):
        print (id_player)
        if id_player in self.games.keys():
            return (1, self.games.get(id_player))
        else:
            return (-1,)
