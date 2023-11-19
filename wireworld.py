from gridcontrol import GridControl

class WireWorld(GridControl):
    def __init__(self, dpi_factor, x, y, w, h, square_size):
        GridControl.__init__(self, dpi_factor, x, y, w, h, square_size)

    def get_cell_state(self, row, col):
        r = row % self.grid_size_x
        c =  col % self.grid_size_y
        return self.current_grid[r][c]

    def set_cell_state_other(self, row, col, state):
        self.other_grid[row][col] = state

    def simulate(self):
        for i in range(self.grid_size_x):
            for j in range(self.grid_size_y):
                current_state = self.get_cell_state(i, j)
                if current_state != 0:
                    if current_state == 1 or current_state == 2:
                        self.set_cell_state_other(i,j,current_state+1)
                    elif current_state == 3:
                        neighbour_heads = 0
                        for p in range(-1,2):
                            for q in range(-1,2):
                                if (p == 0 and q == 0): continue
                                if self.get_cell_state(i+p, j+q) == 1:
                                    neighbour_heads += 1
                        if 1 <= neighbour_heads <= 2:
                            self.set_cell_state_other(i,j,1)
                        else:
                            self.set_cell_state_other(i,j,3)
        self.switch_grids()
        return False

        
