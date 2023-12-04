import util as ut
import random
from functools import cache


@cache
def game_of_life_transform(alive_neighbors, state):
    live_num = len(alive_neighbors)
    if state:  # cell is alive
        if 2 <= live_num <= 3:  # cell stays alive
            return state
        else:
            return 0
    else:  # cell is dead
        if live_num == 3:  # cell becomes alive, pick the color of the majority of neighbors
            cnt_list = [0 for i in range(ut.MOD)]
            for c in alive_neighbors:
                cnt_list[c] += 1
            max_cnt = max(cnt_list)
            return random.choice([c for c in range(1, ut.MOD) if cnt_list[c] == max_cnt])  # pick at random if tie
        else:
            return 0
