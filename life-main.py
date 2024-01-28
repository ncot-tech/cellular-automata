#!/usr/bin/env python3

import pygame
import sys
import conwaylife
import menubar

current_state = 0
show_grid = True

def state0():
    global current_state
    current_state = 0
def state1():
    global current_state
    current_state = 1
def start_sim():
    global simulating
    simulating = not simulating
def reset_sim():
    global simulating,cycle
    simulating = False
    cycle = 0
    grid_control.reset_grids()
def toggle_grid():
    global show_grid
    show_grid = not show_grid

# Initialize Pygame
pygame.init()

# Set up display
display_info = pygame.display.Info()

dpi_factor = 2
width, height = int(800), int(600)

screen = pygame.display.set_mode((width * dpi_factor, height * dpi_factor))
pygame.display.set_caption("Conway's Life Cellular Automaton")

font = pygame.font.SysFont(None, 16)
cycle_text = font.render("", True, (64,64,64))

menu_height = 16
menu = menubar.MenuBar(dpi_factor,0,0,width,menu_height)
menu.add_item((32,32,32), "Dead", state0)
menu.add_item((32,32,32), "Alive", state1)
menu.add_item((0,32,0), "Run / Stop", start_sim)
menu.add_item((32,0,0), "Reset", reset_sim)
menu.add_item((32,0,0), "Grid", toggle_grid)

grid_control = conwaylife.ConwayLife(dpi_factor,0, menu_height, width, height-menu_height, 8)
grid_states = [(0,0,0),(0,255,0)]
grid_control.define_states(grid_states)

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

mouse_x, mouse_y = 0, 0  # Initialize mouse coordinates
# Main loop
simulating = False
running = True
cycle = 0
dragging = False
while running:
    # Handle events
    mouse_x, mouse_y = pygame.mouse.get_pos()
    menu.update(mouse_x, mouse_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button clicked
            if mouse_y <= menu_height * dpi_factor:
                menu.process_click()
            else:
                dragging = True
                grid_control.set_grid_cell_mouse(mouse_x, mouse_y, current_state)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                grid_control.set_grid_cell_mouse(mouse_x, mouse_y, current_state)

    if (simulating):
        grid_control.simulate()
        cycle += 1
        cycle_text = font.render(f"Cycle {cycle}", True, (64,64,64))
    # Update display
    menu.draw(screen)
    screen.blit(cycle_text, (500,8))
    grid_control.draw(screen, show_grid)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

