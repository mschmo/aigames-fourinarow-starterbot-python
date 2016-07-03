import random
from .base_bot import BaseBot


class AlwaysOnTopBot(BaseBot):
    """ Always drops piece on top of opponent
        If opponent doesn't have exposed piece, drop at random
    """

    def make_turn(self):
        opp_spots = []
        prev_zero_spots = []
        for row in self.board:
            new_zero_spots = []
            for i, col_val in enumerate(row):
                if col_val not in (0, self.settings['your_botid']):
                    opp_spots.append(i)
                elif col_val == 0:
                    new_zero_spots.append(i)
            matches = filter(lambda x: x in prev_zero_spots, opp_spots)
            if matches:
                if len(matches) == 1:
                    return self.place_disc(matches[0])
                return self.place_disc(random.choice(matches))
            prev_zero_spots = new_zero_spots
        return self.place_disc(random.randrange(7))
