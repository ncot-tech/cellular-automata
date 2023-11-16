class Rule110:
    def __init__(self, rows, columns, grid):
        self.rows = rows
        self.columns = columns
        self.grid = grid
        self.current_row = 0

    def step(self):
        next_row = self.current_row + 1
        if next_row == self.rows:
            self.current_row = 0
            return False

        for x in range(self.columns-3):
            a = self.grid[x][self.current_row]
            b = self.grid[x+1][self.current_row]
            c = self.grid[x+2][self.current_row]

            # Rule 90 - draws sierpinski triangle
            #self.grid[x+1][next_row] = a ^ c
            
            # Rule 30 - draws shell pattern thing
            self.grid[x+1][next_row] = a ^ (b | c)

            # Rule 184 - to be coded, does traffic somehow


            # Rule 110
            #if (a == 1 and b == 1 and c == 1):
            #    self.grid[x+1][next_row] = 0
            #elif (a == 1 and b == 1 and c == 0):
            #    self.grid[x+1][next_row] = 1
            #elif (a == 1 and b == 0 and c == 1):
            #    self.grid[x+1][next_row] = 1
            #elif (a == 1 and b == 0 and c == 0):
            #    self.grid[x+1][next_row] = 0
            #elif (a == 0 and b == 1 and c == 1):
            #    self.grid[x+1][next_row] = 1
            #elif (a == 0 and b == 1 and c == 0):
            #    self.grid[x+1][next_row] = 1
            #elif (a == 0 and b == 0 and c == 1):
            #    self.grid[x+1][next_row] = 1
            #elif (a == 0 and b == 0 and c == 0):
            #    self.grid[x+1][next_row] = 0

        self.current_row = next_row
        
        return True
