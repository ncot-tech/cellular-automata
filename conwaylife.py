from gridcontrol import GridControl

class ConwayLife(GridControl):
    def __init__(self, dpi_factor, x, y, w, h, square_size):
        GridControl.__init__(self, dpi_factor, x, y, w, h, square_size)

    def get_cell_state(self, row, col):
        r = row % self.grid_size_x
        c =  col % self.grid_size_y
        return self.current_grid[r][c]

    def set_cell_state_other(self, row, col, state):
        self.other_grid[row][col] = state

    def count_neighbours(self, row, col):
        live_neighbours = 0
        for p in range(-1,2):
            for q in range(-1,2):
                if (p == 0 and q == 0): continue
                if self.get_cell_state(row+p, col+q) == 1:
                    live_neighbours += 1
        return live_neighbours


    def simulate(self):
        for i in range(self.grid_size_x):
            for j in range(self.grid_size_y):
                live_neighbours = self.count_neighbours(i, j)
                current_state = self.get_cell_state(i, j)

                if current_state == 0:
                    if live_neighbours == 3:
                        self.set_cell_state_other(i,j,1)    # live
                    else:
                        self.set_cell_state_other(i,j,0)    # Stay dead
                else:
                    if live_neighbours < 2:
                        self.set_cell_state_other(i,j,0)    # die
                    elif live_neighbours == 2 or live_neighbours == 3:
                        self.set_cell_state_other(i,j,1)    # live
                    elif live_neighbours > 3:
                        self.set_cell_state_other(i,j,0)    # die
        self.switch_grids()
        return False

        
