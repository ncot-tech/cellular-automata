#!/usr/bin/env python3

import pygame
import sys
import grid_2d

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

grid_2d.setup(dpi_factor, 2, 8, 3, width, height)

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (0, 255, 255)

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

mouse_x, mouse_y = 0, 0  # Initialize mouse coordinates
# Main loop
running = True
while running:
    # Handle events
    mouse_x, mouse_y = pygame.mouse.get_pos()
    grid_2d.update_highlight(mouse_x, mouse_y)    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button clicked
            # Get mouse position

            grid_2d.toggle_grid_cell(mouse_x, mouse_y)

       # Update display
    screen.fill(black)

    grid_2d.draw_grid(screen)
    grid_2d.draw_highlight(screen)
    grid_2d.draw_magnified_view(screen, mouse_x, mouse_y)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

