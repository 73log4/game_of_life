from grid_object import Grid
import util as ut
import pygame


class GameDisplay:

    def __init__(self, start_grid):
        self.grid = Grid(start_grid)
        self.screen = None

        self.game_paused = True
        self.draw_mode = 1  # the color to draw

        self.time = pygame.time.get_ticks()

        # for long press on arrow keys
        self.right_arrow_pressed = False
        self.left_arrow_pressed = False
        self.key_time = None

    @staticmethod
    def get_grid_position(display_i, display_j):
        return display_j // ut.SQUARE_SIZE, display_i // ut.SQUARE_SIZE

    def draw_grid(self):
        self.draw_grid_rect()
        self.draw_grid_lines()
        self.draw_play_pause_icons()

    def draw_grid_rect(self):
        for i in range(self.grid.dim_1):
            for j in range(self.grid.dim_2):
                square = (j * ut.SQUARE_SIZE, i * ut.SQUARE_SIZE, ut.SQUARE_SIZE, ut.SQUARE_SIZE)
                color = ut.COLORS[self.grid[i][j]]
                pygame.draw.rect(self.screen, color, square)

    def draw_grid_lines(self):
        for i in range(self.grid.dim_2):
            start_pos, end_pos = (i * ut.SQUARE_SIZE, 0), (i * ut.SQUARE_SIZE, ut.SCREEN_SIZE[1])
            pygame.draw.line(self.screen, ut.LINE_COLOR, start_pos, end_pos, ut.LINE_WIDTH)

        for j in range(self.grid.dim_1):
            start_pos, end_pos = (0, j * ut.SQUARE_SIZE), (ut.SCREEN_SIZE[0], j * ut.SQUARE_SIZE)
            pygame.draw.line(self.screen, ut.LINE_COLOR, start_pos, end_pos, ut.LINE_WIDTH)

    def draw_play_pause_icons(self):
        if self.game_paused:
            icon = pygame.image.load('pause_icon.png')
        else:
            icon = pygame.image.load('play_icon.png')
        self.screen.blit(icon, ut.PAUSE_PLAY_POS)

    def change_position(self, i, j):
        if self.grid[i][j] != 0:
            self.grid.edit_position_on_grid(i, j, 0)
        else:
            self.grid.edit_position_on_grid(i, j, self.draw_mode)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # pause/play game
                    self.game_paused = not self.game_paused
                elif event.key in ut.VALID_COLORS:  # change the color to draw when right click is pressed
                    if ut.VALID_COLORS[event.key] < ut.MOD:
                        self.draw_mode = ut.VALID_COLORS[event.key]
                elif event.key == pygame.K_RIGHT:  # go to the next state in the transform
                    self.grid.transform()
                    self.right_arrow_pressed = True
                    self.key_time = pygame.time.get_ticks()
                elif event.key == pygame.K_LEFT:  # go to the last state in the transform
                    self.grid.reverse_transform()
                    self.left_arrow_pressed = True
                    self.key_time = pygame.time.get_ticks()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.right_arrow_pressed = False
                elif event.key == pygame.K_LEFT:
                    self.left_arrow_pressed = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # only left click counts
                if self.game_paused:  # draw on grid
                    mouse = pygame.mouse.get_pos()
                    self.change_position(*self.get_grid_position(*mouse))

        # for long press on arrow keys
        if self.game_paused:
            if self.right_arrow_pressed or self.left_arrow_pressed:
                if pygame.time.get_ticks() - self.key_time > ut.LONG_KEY_PRESS_INTERVAL:
                    if self.right_arrow_pressed:
                        self.grid.transform()
                    else:
                        self.grid.reverse_transform()

    def initialize_display(self):
        pygame.display.set_caption('Game of Life  ' + ut.VERSION)
        tab_icon = pygame.image.load('tab_icon.png')
        pygame.display.set_icon(tab_icon)
        self.screen.fill(ut.COLORS[0])

    def delay(self):
        pygame.time.wait(ut.GAME_TICK)

    def run_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode(ut.SCREEN_SIZE)
        self.initialize_display()

        while True:
            # check if quit game
            if self.process_events() == -1:
                return

            # draw grid
            self.draw_grid()

            # check if game is running or paused
            if not self.game_paused:
                self.grid.transform()

            # delay game by the amount left to fill game ticks
            self.delay()

            # update pygame display
            pygame.display.update()
