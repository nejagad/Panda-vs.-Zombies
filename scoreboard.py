import pygame.font

class Scoreboard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        self.text_color = (255, 183, 197)
        self.font = pygame.font.SysFont(None, 48)
        self.font2 = pygame.font.SysFont(None, 24)

        self.prep_score()
        self.prep_high_score()
        self.prep_lives()

    def prep_lives(self):
         lives_str = "Lives Left: " + str(self.stats.pandas_left)
         self.lives_image = self.font.render(lives_str, True, self.text_color, self.settings.bg_color)
         self.lives_rect = self.lives_image.get_rect()
         self.lives_rect.left = self.screen_rect.left + 10
         self.lives_rect.top = 60


    def prep_score(self):
            score_str = "Score: " + str(self.stats.score)
            self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

            self.score_rect = self.score_image.get_rect()
            self.score_rect.right = self.screen_rect.right - 20
            self.score_rect.top = 20

    def prep_high_score(self):
         high_score = self.stats.high_score
         high_score_str = "High Score: " + "{:,}".format(high_score)
         self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

         self.high_score_rect = self.high_score_image.get_rect()
         self.high_score_rect.right = self.screen_rect.right - 20
         self.high_score_rect.top = 60
 
    def show_score(self):
         self.screen.blit(self.score_image, self.score_rect)
         self.screen.blit(self.high_score_image, self.high_score_rect)
         self.screen.blit(self.lives_image, self.lives_rect)

    def check_high_score(self):
         if self.stats.score > self.stats.high_score:
              self.stats.high_score = self.stats.score
              self.prep_high_score()