import pygame

class Panda:
    
    def __init__(self, ai_game): # takes in self reference and reference to current instance of AlienInvasion class
                                # gives panda access to all game resources defined in AlienInvasion

        self.screen = ai_game.screen # assigns screen to an attribute of panda so we can easily access it in all
                                        # methods of the class
    
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect() # access rect attribute and assigning it

        self.image = pygame.image.load('images/panda.png') # load panda image
        self.rect = self.image.get_rect() # gets its rectangle (what we treat each element as)

        self.rect.midtop = self.screen_rect.midtop # starts each new panda at bottom center of screen

        self.x = float(self.rect.x) # stores a decimal value for panda's horizontal position
        
        self.moving_right = False # movement flag
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.panda_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.panda_speed

        self.rect.x = self.x

    def center_panda(self):
        self.rect.midtop = self.screen_rect.midtop
        self.x = float(self.rect.x)

    def blitme(self):

        self.screen.blit(self.image, self.rect) # draws image to screen at the position specificed by self.rect
