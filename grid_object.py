import copy
import util as ut
from functools import cache
from transform_functions import game_of_life_transform
from grid_music import GridMusic


class GridHistory:

    def __init__(self, start_grid):
        self.history = [(start_grid, 'transform')]  # 'transform' for node that was reached by transform, 'edit' otherwise
        self.location = 0

    def next_node_is_transform(self):
        return self.location < len(self.history) - 1 and self.history[self.location + 1][1] == 'transform'

    def current_grid(self):
        return self.history[self.location][0]

    def add_edit(self, edit_grid):
        self.history = self.history[:self.location + 1]  # cut the rest of the history
        self.history.append((edit_grid, 'edit'))
        self.location += 1

    def add_transform(self, transform_grid):
        if not self.next_node_is_transform():
            self.history = self.history[:self.location + 1]  # cut the rest of the history
            self.history.append((transform_grid, 'transform'))
        self.location += 1

    def next(self):
        if self.next_node_is_transform():
            self.location += 1
            return self.current_grid()
        else:
            return None

    def previous(self):
        self.location = max(0, self.location - 1)
        return self.current_grid()


class Grid:

    def __init__(self, start_grid):
        self.grid = start_grid
        self.music = GridMusic()

        self.dim_1, self.dim_2 = len(self.grid), len(self.grid[1])

        self.history = GridHistory(copy.deepcopy(start_grid))

        self.alive_cells = self.count_alive_cells()


    def __str__(self):
        grid_str = ''

        for i in range(self.dim_1):
            for j in range(self.dim_2):
                grid_str += str(self.grid[i][j]) + ' '
            grid_str += '\n'

        return grid_str[:-1]  # remove lats new line character

    def __getitem__(self, key):
        return self.grid[key]

    def count_alive_cells(self):
        cnt = 0
        for i in range(self.dim_1):
            for j in range(self.dim_2):
                if self.grid[i][j]:
                    cnt += 1
        return cnt

    def play_sound(self):
        if ut.SOUND_ON:
            self.music.play_sound(self.alive_cells)

    @cache
    def valid_key(self, i, j):
        return 0 <= i < self.dim_1 and 0 <= j < self.dim_2

    def edit_position_on_grid(self, i, j, new_state):
        old_state = self.grid[i][j]
        if old_state and new_state == 0:
            self.alive_cells -= 1
        elif old_state == 0 and 0:
            self.alive_cells += 1
        self.grid[i][j] = new_state
        self.history.add_edit(copy.deepcopy(self.grid))
        self.play_sound()

    def get_alive_neighbors(self, i, j):
        neighbors = []
        for k, m in ut.DIRECTIONS:
            if self.valid_key(i + k, j + m) and self.grid[i + k][j + m]:
                neighbors.append(self.grid[i + k][j + m])
        return tuple(neighbors)

    def transform(self):
        next_grid = self.history.next()
        if next_grid:  # next() did not return None, use cached grid
            self.grid = next_grid
        else:  # calculate new grid transform
            new_grid = copy.deepcopy(self.grid)
            for i in range(self.dim_1):
                for j in range(self.dim_2):
                    neighbors = self.get_alive_neighbors(i, j)
                    new_grid[i][j] = game_of_life_transform(neighbors, self.grid[i][j])
            self.grid = new_grid
            self.history.add_transform(copy.deepcopy(self.grid))

        self.alive_cells = self.count_alive_cells()
        self.play_sound()

    def reverse_transform(self):
        new_grid = self.history.previous()
        self.grid = self.history.previous()
        self.alive_cells = self.count_alive_cells()
        self.play_sound()
