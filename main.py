import util
from grid_object import Grid
from transform_functions import *
import pygame
from display import GameDisplay
import random
import util as ut
from settings_interface import Settings

def start_game():
    print('Start')
    n, m = ut.SCREEN_SIZE[0] // ut.SQUARE_SIZE, ut.SCREEN_SIZE[1] // ut.SQUARE_SIZE
    random_start_list = [i for i in range(1, ut.MOD)] + [0] * ut.MOD * 2
    start_grid_2 = [[random.choice(random_start_list) for i in range(n)] for j in range(m)]
    start_grid_1 = [[0 for i in range(n)] for j in range(m)]

    game = GameDisplay(start_grid_2)
    game.run_game()

st = Settings(start_game)
