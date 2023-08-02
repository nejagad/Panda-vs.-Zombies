import pygame.font

class Button:

    def __init__(self, ai_game, msg):

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50   # setting dimensions & properties of button
        self.button_color = (60,179,113)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0,0, self.width, self.height) # building button's rect object and centering
        self.rect.center = self.screen_rect.center
        self.rect.top = 200

        self._prep_msg(msg)

    def _prep_msg(self, msg):   # turns text into an image
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.msg_image_rect.top = 200
    
    def draw_button(self):  # displays button onscreen
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)