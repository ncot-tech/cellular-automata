import pygame

class MenuBar:
    def __init__(self, dpi_factor, x, y, w, h):
        self.menu_items = []
        self.x = x * dpi_factor
        self.y = y * dpi_factor
        self.w = w * dpi_factor
        self.h = h * dpi_factor
        self.dpi_factor = dpi_factor
        self.surface = pygame.Surface((self.w, self.h))

    def add_item(self, colour, callback = None):
        self.menu_items.append({"colour": colour, "cb" : callback, "highlight" : False })

    def update(self, mouse_x, mouse_y):
        for i in range(len(self.menu_items)):
            x = self.x + (i * (16 + 2) * self.dpi_factor)
            y = self.y
            w = x + (16 * self.dpi_factor)
            h = y + (16 * self.dpi_factor)
            if x <= mouse_x <= w and y <= mouse_y <= h:
                self.menu_items[i]['highlight'] = True
            else:
                self.menu_items[i]['highlight'] = False

    def process_click(self):
        for i in range(len(self.menu_items)):
            if self.menu_items[i]['highlight'] == True:
                if self.menu_items[i]['cb'] != None:
                    self.menu_items[i]['cb']()

    def draw(self, screen):
        self.surface.fill((200,200,200))
        for i in range(len(self.menu_items)):
            if self.menu_items[i] != None:
                colour = self.menu_items[i]['colour']
                if self.menu_items[i]['highlight']:
                    colour = (255,255,255)
                pygame.draw.rect(self.surface, colour, (i * (16 + 2) * self.dpi_factor, 0, 16 * self.dpi_factor, 16 * self.dpi_factor))
        screen.blit(self.surface, (0, 0))
