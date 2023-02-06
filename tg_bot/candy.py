import random as rnd


class Candy:

    def __init__(self, name: str = 'Anonyme'):
        self.candy_count = rnd.randint(150, 300)
        self.max_for_step = rnd.randint(10, 30)
        self.beginer = rnd.randint(0, 1)
        self.is_game_on = 1
        self.player = name
        self.game_done = 0

    def bot_AI(self):
        if self.candy_count == 0:
            return -1
        return rnd.randint(1, min(self.candy_count, self.max_for_step)) if self.candy_count % (self.max_for_step + 1) == 0 else self.candy_count % (self.max_for_step + 1)

    def make_step(self, count: int):
        if not self.is_game_on:
            return
        if self.candy_count == 0:
            self.is_game_on = 0
            return

        if count >= self.candy_count:
            self.candy_count = 0
            self.is_game_on = 0
            return

        else:
            self.candy_count -= count
            self.beginer += 1
            return

    def restart(self):
        self.candy_count = rnd.randint(100, 200)
        self.max_for_step = rnd.randint(10, 30)
        self.beginer = rnd.randint(0, 1)
        self.is_game_on = 1
        self.game_done += 1
        print(f'{self.player}   {self.game_done}')

    def end_game(self):
        pass

    def get_candy_count(self):
        return self.candy_count

    def get_candy_max(self):
        return self.max_for_step

    def get_beginer(self):
        return self.beginer

    def set_player(self, name: str):
        self.player = name

    def get_player(self):
        return self.player

    def get_player_game_done(self):
        return self.game_done

    def is_game(self):
        return self.is_game_on
    def game_done(self):
        return self.game_done
