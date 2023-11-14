#!/usr/bin/env python3

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
#width, height = 800, 600
# Set up display
display_info = pygame.display.Info()
print (display_info)

dpi_factor = 2
width, height = int(800 * dpi_factor), int(600 * dpi_factor)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Basic Pygame Program")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (0, 255, 255)

# Set up grid parameters
grid_size = 8 * dpi_factor
square_size = 8 * dpi_factor
gap_size = 2 * dpi_factor


# Calculate grid size based on screen dimensions and square size
grid_size_x = (width + gap_size) // (square_size + gap_size)
grid_size_y = (height + gap_size) // (square_size + gap_size)

# Recalculate gap size to fit the screen exactly
gap_size_x = (width - (grid_size_x * square_size)) // (grid_size_x - 1)
gap_size_y = (height - (grid_size_y * square_size)) // (grid_size_y - 1)

# Create a 2D array to track the state of each square (0 for white, 1 for red)
grid_state = [[0] * grid_size_y for _ in range(grid_size_x)]

# Set up magnified view parameters
magnify_factor = 3
magnified_size = square_size * magnify_factor
magnified_grid_x = (magnified_size + gap_size) * 3
magnified_grid_y = (magnified_size + gap_size) * 3
magnified_surface = pygame.Surface((magnified_grid_x, magnified_grid_y))
print (f"Magnified size {magnified_grid_x}")
# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

mouse_x, mouse_y = 0, 0  # Initialize mouse coordinates
clicked_row, clicked_col = 0, 0
highlighted_row, highlighted_col = 0, 0

# Main loop
running = True
while running:
    # Handle events
    mouse_x, mouse_y = pygame.mouse.get_pos()
    highlighted_row = mouse_x // (square_size + gap_size_x)
    highlighted_col = mouse_y // (square_size + gap_size_y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button clicked
            # Get mouse position

            # Determine the clicked square and toggle its state
            clicked_row = mouse_x // (square_size + gap_size_x)
            clicked_col = mouse_y // (square_size + gap_size_y)
            if 0 <= clicked_row < grid_size_x and 0 <= clicked_col < grid_size_y:
                grid_state[clicked_row][clicked_col] = 1 - grid_state[clicked_row][clicked_col]

    # Update display
    screen.fill(black)
    #pygame.draw.circle(screen, white, (mouse_x, mouse_y), 20)  # Draw a circle at the mouse position

    # Draw grid
    for i in range(grid_size_x):
        for j in range(grid_size_y):
            x = i * (square_size + gap_size_x)
            y = j * (square_size + gap_size_y)

            # Check the state of the square and draw accordingly
            if grid_state[i][j] == 1:
                pygame.draw.rect(screen, red, (x, y, square_size, square_size))
            else:
                pygame.draw.rect(screen, white, (x, y, square_size, square_size))

    pygame.draw.rect(screen, yellow, (highlighted_row * (square_size + gap_size_x), highlighted_col * (square_size + gap_size_y), square_size, square_size))

    # Update magnified view
    #magnified_view = pygame.Rect(0, 0, magnified_size, magnified_size)
    magnified_surface.fill(black)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= highlighted_row + i < grid_size_x and 0 <= highlighted_col + j < grid_size_y:
                if grid_state[highlighted_row + i][highlighted_col + j] == 1:
                    pygame.draw.rect(magnified_surface, red, ((i+1) * (magnified_size + gap_size), (j+1) * (magnified_size + gap_size), magnified_size, magnified_size))
                else:
                    pygame.draw.rect(magnified_surface, white, ((i+1) * (magnified_size + gap_size), (j+1) * (magnified_size + gap_size), magnified_size, magnified_size))
            else:
                pygame.draw.rect(magnified_surface, white, ((i+1) * (magnified_size + gap_size), (j+1) * (magnified_size + gap_size), magnified_size, magnified_size))

    # Draw magnified view in the top right corner or top left if mouse in the way
    if (mouse_x >= width - magnified_grid_x and mouse_y < magnified_grid_y):
        screen.blit(magnified_surface, (0, 0))
    else:
        screen.blit(magnified_surface, (width - magnified_grid_x, 0))



    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

