import random
from .base_bot import BaseBot


class RandomBot(BaseBot):

    def make_turn(self):
        self.place_disc(random.randrange(7))
