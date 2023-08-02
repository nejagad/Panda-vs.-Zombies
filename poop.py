import pygame
from pygame.sprite import Sprite

class Poop(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.poop_color

        self.rect = pygame.Rect(0, 80, self.settings.poop_width, self.settings.poop_height) # creates poop at 0,0
        self.rect.center = ai_game.panda.rect.center
        self.rect.y = 84

        self.y = float(self.rect.y) # stores poop position as a decimal value
        self.moving = False

    def update(self):
        self.y += self.settings.poop_speed # updates decimal position of the poop
        self.rect.y = self.y # updates rect position

    def draw_poop(self):
            pygame.draw.rect(self.screen, self.color, self.rect)

    

    