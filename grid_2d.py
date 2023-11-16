
import pygame

# Size in pixels of one square
# Size in pixels of the gap between squares
_square_size, _gap_size_x, _gap_size_y = 0,0,0

# The number of squares across and down in the grid
grid_size_x, grid_size_y = 0, 0
_gap_size_x, _gap_size_y = 0, 0
_magnified_square_size = 0
_magnified_grid_size_x, _magnified_grid_size_y = 0, 0
_magnified_surface = None

_clicked_row, _clicked_col = 0, 0
_highlighted_row, _highlighted_col = 0, 0

grid_state = []

_set_colour = (255, 0, 0)
_clear_colour = (255, 255, 255)
_highlight_colour = (255, 255, 0)
_black = (0, 0, 0)

_screen_width = 0
_screen_height = 0

def setup(dpi_factor, gap_size, square_size, magnify_factor, screen_width, screen_height):
    global _square_size, _magnified_square_size
    global _magnified_grid_size_x, _magnified_grid_size_y
    global _magnified_surface, grid_size_x, grid_size_y
    global grid_state, _gap_size_x, _gap_size_y
    global _screen_width, _screen_height

    _screen_width = screen_width
    _screen_height = screen_height

    # Set up grid parameters
    _square_size = square_size * dpi_factor
    gap_size = gap_size * dpi_factor

    # Calculate grid size based on screen dimensions and square size
    grid_size_x = (screen_width + gap_size) // (_square_size + gap_size)
    grid_size_y = (screen_height + gap_size) // (_square_size + gap_size)

    # Recalculate gap size to fit the screen exactly
    _gap_size_x = (screen_width - (grid_size_x * _square_size)) // (grid_size_x - 1)
    _gap_size_y = (screen_height - (grid_size_y * _square_size)) // (grid_size_y - 1)

    # Create a 2D array to track the state of each square (0 for white, 1 for red)
    grid_state = [[0] * grid_size_y for _ in range(grid_size_x)]

    # Set up magnified view parameters
    _magnified_square_size = _square_size * magnify_factor
    _magnified_grid_size_x = (_magnified_square_size + gap_size) * 3
    _magnified_grid_size_y = (_magnified_square_size + gap_size) * 3
    _magnified_surface = pygame.Surface((_magnified_grid_size_x, _magnified_grid_size_y))

def clear():
    for x in range(grid_size_x):
        for y in range(grid_size_y):
            grid_state[x][y] = 0

def update_highlight(mouse_x, mouse_y):
    global _highlighted_row, _highlighted_col

    _highlighted_row = mouse_x // (_square_size + _gap_size_x)
    _highlighted_col = mouse_y // (_square_size + _gap_size_y)

def toggle_grid_cell(mouse_x, mouse_y):
    global grid_state
    # Determine the clicked square and toggle its state
    clicked_row = mouse_x // (_square_size + _gap_size_x)
    clicked_col = mouse_y // (_square_size + _gap_size_y)
    if 0 <= clicked_row < grid_size_x and 0 <= clicked_col < grid_size_y:
        grid_state[clicked_row][clicked_col] = 1 - grid_state[clicked_row][clicked_col]

# Draw grid
def draw_grid(screen):
    for i in range(grid_size_x):
        for j in range(grid_size_y):
            x = i * (_square_size + _gap_size_x)
            y = j * (_square_size + _gap_size_y)

            # Check the state of the square and draw accordingly
            try:
                if grid_state[i][j] == 1:
                    pygame.draw.rect(screen, _set_colour, (x, y, _square_size, _square_size))
                else:
                    pygame.draw.rect(screen, _clear_colour, (x, y, _square_size, _square_size))
            except:
                print (f"Oops {i},{j} doesn't exist")
                exit(1)

def draw_highlight(screen):
    pygame.draw.rect(screen, _highlight_colour, (_highlighted_row * (_square_size + _gap_size_x), _highlighted_col * (_square_size + _gap_size_y), _square_size, _square_size))

def draw_magnified_view(screen, mouse_x, mouse_y):
    _magnified_surface.fill(_black)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= _highlighted_row + i < grid_size_x and 0 <= _highlighted_col + j < grid_size_y:
                if grid_state[_highlighted_row + i][_highlighted_col + j] == 1:
                    pygame.draw.rect(_magnified_surface, _set_colour, ((i+1) * (_magnified_square_size + _gap_size_x), (j+1) * (_magnified_square_size + _gap_size_y), _magnified_square_size, _magnified_square_size))
                else:
                    pygame.draw.rect(_magnified_surface, _clear_colour, ((i+1) * (_magnified_square_size + _gap_size_x), (j+1) * (_magnified_square_size + _gap_size_y), _magnified_square_size, _magnified_square_size))
            else:
                pygame.draw.rect(_magnified_surface, _clear_colour, ((i+1) * (_magnified_square_size + _gap_size_x), (j+1) * (_magnified_square_size + _gap_size_y), _magnified_square_size, _magnified_square_size))

    # Draw magnified view in the top right corner or top left if mouse in the way
    if (mouse_x >= _screen_width - _magnified_grid_size_x and mouse_y < _magnified_grid_size_y):
        screen.blit(_magnified_surface, (0, 0))
    else:
        screen.blit(_magnified_surface, (_screen_width - _magnified_grid_size_x, 0))
 

