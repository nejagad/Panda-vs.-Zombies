import pygame
# from PIL import Image, ImageDraw
# import textwrap


class Help:
    def __init__(self, ai_game, msg):

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 2000, 5000   # setting dimensions & properties of button
        self.button_color = (32, 42, 68)
        self.text_color = (255, 183, 197)
        self.font = pygame.font.SysFont(None, 30)

        self.rect = pygame.Rect(0,0, self.width, self.height) # building button's rect object and centering
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):   # turns text into an image
        # draw.multiline_text((self.screen_rect.width, self.screen_rect.height), msg, fill = self.button_color, font = self.font)
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.msg_image_rect.top = 360

        self.msg2_image = self.font.render("Use the left and right arrow keys to move back and forth and the space bars to release a deadly poop. Use the X key to quit at any time.", True, self.text_color, self.button_color)
        self.msg2_image_rect = self.msg2_image.get_rect()
        self.msg2_image_rect.center = self.rect.center
        self.msg2_image_rect.top = 460


        self.msg3_image = self.font.render("Ready for your mission? Press the P key to begin. Best of luck!", True, self.text_color, self.button_color)
        self.msg3_image_rect = self.msg3_image.get_rect() 
        self.msg3_image_rect.center = self.rect.center
        self.msg3_image_rect.top = 560
      
    
    def draw_button(self):  # displays button onscreen
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.msg2_image, self.msg2_image_rect)
        self.screen.blit(self.msg3_image, self.msg3_image_rect)
