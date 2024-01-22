from gridcontrol import GridControl

class OneDCA(GridControl):
    def __init__(self, dpi_factor, x, y, w, h, square_size):
        GridControl.__init__(self, dpi_factor, x, y, w, h, square_size)
        self.current_row = 0
        
    def get_cell_state(self, row, col):
        r = row % self.grid_size_x
        c =  col % self.grid_size_y
        return self.current_grid[r][c]
    def set_cell_state(self, row, col,state):
        self.current_grid[row][col] = state

class Rule30(OneDCA):
    def simulate(self):
        next_row = self.current_row + 1
        if next_row == self.grid_size_y:
            self.current_row = 0
            return False

        for x in range(self.grid_size_x-3):
            a = self.get_cell_state(x, self.current_row)
            b = self.get_cell_state(x+1, self.current_row)
            c = self.get_cell_state(x+2, self.current_row)

            # Rule 30 - draws shell pattern thing
            self.set_cell_state(x+1, next_row, a ^ (b | c))
        self.current_row = next_row
        
        return True

class Rule90(OneDCA):
    def simulate(self):
        next_row = self.current_row + 1
        if next_row == self.grid_size_y:
            self.current_row = 0
            return False

        for x in range(self.grid_size_x-3):
            a = self.get_cell_state(x, self.current_row)
            b = self.get_cell_state(x+1, self.current_row)
            c = self.get_cell_state(x+2, self.current_row)

            # Rule 90 - draws sierpinski triangle
            self.set_cell_state(x+1, next_row, a ^ c)
            
        self.current_row = next_row
        
        return True
 
class Rule110(OneDCA):
    def simulate(self):
        next_row = self.current_row + 1
        if next_row == self.grid_size_y:
            self.current_row = 0
            return False

        for x in range(self.grid_size_x-3):
            a = self.get_cell_state(x, self.current_row)
            b = self.get_cell_state(x+1, self.current_row)
            c = self.get_cell_state(x+2, self.current_row)

           # Rule 110
            if (a == 1 and b == 1 and c == 1):
                self.set_cell_state(x+1,next_row,0)
            elif (a == 1 and b == 1 and c == 0):
                self.set_cell_state(x+1,next_row,1)
            elif (a == 1 and b == 0 and c == 1):
                self.set_cell_state(x+1,next_row,1)
            elif (a == 1 and b == 0 and c == 0):
                self.set_cell_state(x+1,next_row,0)
            elif (a == 0 and b == 1 and c == 1):
                self.set_cell_state(x+1,next_row,1)
            elif (a == 0 and b == 1 and c == 0):
                self.set_cell_state(x+1,next_row,1)
            elif (a == 0 and b == 0 and c == 1):
                self.set_cell_state(x+1,next_row,1)
            elif (a == 0 and b == 0 and c == 0):
                self.set_cell_state(x+1,next_row,0)

        self.current_row = next_row
        
        return True
