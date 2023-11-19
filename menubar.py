import pygame

class MenuBar:
    def __init__(self, dpi_factor, x, y, w, h):
        self.font = pygame.font.SysFont(None, (h - 6) * dpi_factor)
        self.menu_items = []
        self.x = x * dpi_factor
        self.y = y * dpi_factor
        self.w = w * dpi_factor
        self.h = h * dpi_factor
        self.dpi_factor = dpi_factor
        self.surface = pygame.Surface((self.w, self.h))

    def add_item(self, colour, label, callback = None):
        text_surface = self.font.render(label, True, (255,255,255))
        text_rect = text_surface.get_rect()
        text_rect.x += 1 * self.dpi_factor
        text_rect.y += 5 * self.dpi_factor
    
        button_rect = text_surface.get_rect()
        button_rect.h = 14 * self.dpi_factor
        button_rect.w += 2 * self.dpi_factor
        # Calculate where the button goes on the menubar
        xpos = 4
        for button in self.menu_items:
            xpos += button['button_rect'].w + 4
        button_rect.y = 1 * self.dpi_factor
        button_rect.x = xpos
        self.menu_items.append(
                {"colour": colour,
                 "cb" : callback,
                 "highlight" : False,
                 "text_surface" : text_surface,
                 "button_rect" : button_rect,
                 "text_rect" : text_rect})

    def update(self, mouse_x, mouse_y):
        for i in range(len(self.menu_items)):
            button_rect = self.menu_items[i]['button_rect']
            
            if button_rect.x <= mouse_x <= button_rect.x + button_rect.w and button_rect.y <= mouse_y <= button_rect.h + button_rect.y:
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
                button_position = self.menu_items[i]['button_rect']
                text_position = pygame.Rect(self.menu_items[i]['text_rect'])
                text_position.x += button_position.x
                if self.menu_items[i]['highlight']:
                    colour = (255,255,255)
                pygame.draw.rect(self.surface, colour, button_position)
                self.surface.blit(self.menu_items[i]['text_surface'], text_position)
        screen.blit(self.surface, (0, 0))
