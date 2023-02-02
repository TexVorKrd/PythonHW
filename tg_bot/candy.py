import random as rnd


class Candy:

    def __init__(self):
        self.candy_count = rnd.randint(150, 300)
        self.max_for_step = rnd.randint(10, 30)
        self.beginer = rnd.randint(0, 1)

    def bot_AI(self):
        if self.candy_count == 0:
            return -1
        return rnd.randint(1, min(self.candy_count, self.max_for_step)) if self.candy_count % (
                    self.max_for_step + 1) == 0 else self.candy_count % (self.max_for_step + 1)

    def make_step(self, count: int):
        if self.candy_count == 0:
            return -1
        if count > self.candy_count:
            self.candy_count = 0
            return 1
        else:
            self.candy_count -= count
            self.beginer += 1
            return 0

    def restart(self):
        self.candy_count = rnd.randint(150, 300)
        self.max_for_step = rnd.randint(10, 30)
        self.beginer = rnd.randint(0, 1)

    def get_candy_count(self):
        return self.candy_count

    def get_candy_max(self):
        return self.max_for_step

    def get_beginer(self):
        return self.beginer
