import pygame
from pygame.sprite import Sprite

class Zombie(Sprite):
    def __init__(self, ai_game):

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/zombie.png')
        self.rect = self.image.get_rect()
        self.screen_rect = ai_game.screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom 

      #  self.rect.x = self.rect.width
        
        #self.rect.y = 0

        self.x = float(self.rect.x)
    
    def update(self):
        self.x += (self.settings.zombie_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        
                