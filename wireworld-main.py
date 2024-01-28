#!/usr/bin/env python3

import pygame
import sys
import menubar
import wireworld

current_state = 0

def state0():
    global current_state
    current_state = 0
def state1():
    global current_state
    current_state = 1
def state2():
    global current_state
    current_state = 2
def state3():
    global current_state
    current_state = 3
def start_sim():
    global simulating
    simulating = not simulating
def reset_sim():
    global simulating
    simulating = False
    grid_control.reset_grids()

# Initialize Pygame
pygame.init()

# Set up display
display_info = pygame.display.Info()

dpi_factor = 2
width, height = int(800), int(600)

screen = pygame.display.set_mode((width * dpi_factor, height * dpi_factor))
pygame.display.set_caption("Wireworld Cellular Automaton")

font = pygame.font.SysFont(None, 16)
cycle_text = font.render("", True, (64,64,64))

#rule110ca = rule110.Rule110(grid_2d.grid_size_y, grid_2d.grid_size_x, grid_2d.grid_state)

menu_height = 16
menu = menubar.MenuBar(dpi_factor,0,0,width,menu_height)
menu.add_item((32,32,32), "Empty", state0)
menu.add_item((0,0,32), "Head", state1)
menu.add_item((32,0,0), "Tail", state2)
menu.add_item((32,32,0), "Wire", state3)
menu.add_item((0,32,0), "Run / Stop", start_sim)
menu.add_item((32,0,0), "Reset", reset_sim)

grid_control = wireworld.WireWorld(dpi_factor,0, menu_height, width, height-menu_height, 8)
grid_states = [(0,0,0),(0,0,255),(255,0,0),(255,255,0)]
grid_control.define_states(grid_states)

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

mouse_x, mouse_y = 0, 0  # Initialize mouse coordinates
# Main loop
simulating = False
running = True
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
                grid_control.set_grid_cell_mouse(mouse_x, mouse_y, current_state)

    if (simulating):
        grid_control.simulate()
        #simulating = rule110ca.step()
       # Update display
    menu.draw(screen)
    grid_control.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(15)

# Quit Pygame
pygame.quit()
sys.exit()

