from transform_functions import *
import pygame

VERSION = '1.5.2'

#  --------------------- settings ---------------------------


MOD = 8                     # number of total possible states (number of colors + 1)

SCREEN_SIZE = [650, 650]    # size of screen in pixels

SQUARE_SIZE = 13            # size of one square in pixels

GAME_TICK = 50              # game ticks in milliseconds (min of 50 ticks when sound is on)

SOUND_ON = True            # for sound on set to True, for sound off set to False

SOUND_VOLUME = 0.2          # volume of sound from 0 to 1


# --------------------- game constants ---------------------


COLORS = {
    0: (255, 255, 255),
    1: (39, 174, 96),
    2: (241, 196, 15 ),
    3: (244, 67, 54),
    4: (52, 152, 219),
    5: (142, 68, 173),
    6: (251, 140, 0),
    7: (121, 85, 72)
}

VALID_COLORS = {
    pygame.K_1: 1,
    pygame.K_2: 2,
    pygame.K_3: 3,
    pygame.K_4: 4,
    pygame.K_5: 5,
    pygame.K_6: 6,
    pygame.K_7: 7,
}

LINE_COLOR = (210, 210, 210)

LINE_WIDTH = 1

PAUSE_PLAY_POS = (10, 10)

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

LONG_KEY_PRESS_INTERVAL = 250

NUM_OF_CELLS = (SCREEN_SIZE[0] // SQUARE_SIZE) * (SCREEN_SIZE[1] // SQUARE_SIZE)

NOTES = ['A0', 'Bb0', 'B0', 'C1', 'Db1', 'D1', 'Eb1', 'E1', 'F1', 'Gb1', 'G1', 'Ab1',
               'A1', 'Bb1', 'B1', 'C2', 'Db2', 'D2', 'Eb2', 'E2', 'F2', 'Gb2', 'G2', 'Ab2',
               'A2', 'Bb2', 'B2', 'C3', 'Db3', 'D3', 'Eb3', 'E3', 'F3', 'Gb3', 'G3', 'Ab3',
               'A3', 'Bb3', 'B3', 'C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4', 'Gb4', 'G4', 'Ab4',
               'A4', 'Bb4', 'B4', 'C5', 'Db5', 'D5', 'Eb5', 'E5', 'F5', 'Gb5', 'G5', 'Ab5',
               'A5', 'Bb5', 'B5', 'C6', 'Db6', 'D6', 'Eb6', 'E6', 'F6', 'Gb6', 'G6', 'Ab6',
               'A6', 'Bb6', 'B6', 'C7', 'Db7', 'D7', 'Eb7', 'E7', 'F7', 'Gb7', 'G7', 'Ab7',
               'A7', 'Bb7', 'B7', 'C8']

DEFAULT_SETTINGS = [7, 650, 650, 13, 50, 0.5]

SETTINGS_PAD = 40

SETTINGS_SCREEN = (450, 650)

BUTTON_COLOR = '#D0D3D4'

SETTINGS_BG = '#FFFFFF'


