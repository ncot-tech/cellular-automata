import pygame

class GridControl:
    def __init__(self, dpi_factor, x, y, w, h, square_size):
        self.dpi_factor = dpi_factor
        self.w = w * dpi_factor
        self.h = h * dpi_factor
        self.x = x * dpi_factor
        self.y = y * dpi_factor
        self.square_size = square_size * dpi_factor
        self.surface = pygame.Surface((self.w, self.h))

        self.gap_size = 2

        self.grid_size_x = (self.w + self.gap_size) // (self.square_size + self.gap_size)
        self.grid_size_y = (self.h + self.gap_size) // (self.square_size + self.gap_size)

        self.grid_state1 = [[0] * self.grid_size_y for _ in range(self.grid_size_x)]
        self.grid_state2 = [[0] * self.grid_size_y for _ in range(self.grid_size_x)]
        self.grids = [self.grid_state1, self.grid_state2]
        self.current_grid_id = 0
        self.current_grid = self.grids[0]
        self.other_grid = self.grids[1]

    def switch_grids(self):
        # toggle the value between 0 and 1
        self.other_grid = self.grids[self.current_grid_id]
        self.current_grid_id ^= 1
        self.current_grid = self.grids[self.current_grid_id]

    def define_states(self, states):
        self.states = states

    def reset_grids(self):
        self.clear_grid()
        self.switch_grids()
        self.clear_grid()

    def clear_grid(self):
        for x in range(self.grid_size_x):
            for y in range(self.grid_size_y):
                self.current_grid[x][y] = 0

    def set_grid_cell(self, row, col, state):
        if 0 <= row < self.grid_size_x and 0 <= col < self.grid_size_y:
            self.current_grid[row][col] = state

    def set_grid_cell_mouse(self, mouse_x, mouse_y, state):
        clicked_row = (mouse_x - self.x) // (self.square_size + self.gap_size)
        clicked_col = (mouse_y - self.y) // (self.square_size + self.gap_size)

        if 0 <= clicked_row < self.grid_size_x and 0 <= clicked_col < self.grid_size_y:
            self.current_grid[clicked_row][clicked_col] = state

    def draw(self, screen):
        self.surface.fill((64,64,64))

        for i in range(self.grid_size_x):
            for j in range(self.grid_size_y):
                x = i * (self.square_size + self.gap_size)
                y = j * (self.square_size + self.gap_size)

                state = self.current_grid[i][j]
                pygame.draw.rect(self.surface, self.states[state], (x, y, self.square_size, self.square_size))

        screen.blit(self.surface, (self.x, self.y))
