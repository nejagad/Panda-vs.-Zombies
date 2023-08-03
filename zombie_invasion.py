import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from panda import Panda
from poop import Poop
from zombie import Zombie
from button import Button
from scoreboard import Scoreboard
from directions import Directions
from help import Help

class ZombieInvasion:

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

                                                            # object we assign to self.screen = a surface (part of 
                                                            # screen where game element can be displayed)
                                                            # in this case, entire game window
        self.stats = GameStats(self)      
        self.sb = Scoreboard(self)                      
        self.panda = Panda(self) # making an instance of panda
        self.poops = pygame.sprite.Group()
        self.zombies = pygame.sprite.Group()

        self._create_fleet()
        self.play_button = Button(self, "PLAY GAME")
        self.question_button = Directions(self, "Press X to exit")
        str1 = "Your mission is to save the world by guiding the panda to poop on all the zombies and kill them. Your panda has 3 lives."
        self.help_button = Help(self, str1)
        self.over_button = Button(self, "GAME OVER")
        self.win_button = Button(self, "YOU WON!")
        

    def run_game(self):

        while True:
            self._check_events()
            if self.stats.game_active :
                  self.panda.update()
                  self._update_poops()
                  self._update_zombies()

            self._update_screen()

            for poop in self.poops.copy():
                  if poop.rect.bottom <= 0:
                        self.poops.remove(poop)

    def _check_events(self):
           for event in pygame.event.get(): # to access events that Pygame detects, returns list of events that have taken
                                            # place since last time function was called
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
            
                elif event.type == pygame.MOUSEBUTTONDOWN:
                      mouse_pos = pygame.mouse.get_pos()
                      self._check_play_button(mouse_pos)
                      self._check_question_button(mouse_pos)
            
              
                    

    def _check_keydown_events(self, event):
                    if event.key == pygame.K_RIGHT:
                          self.panda.moving_right = True
                    elif event.key == pygame.K_LEFT:
                          self.panda.moving_left = True
                    elif event.key == pygame.K_x:
                          sys.exit()
                    elif event.key == pygame.K_SPACE:

                        self._fire_poop()
                    
                    elif event.key == pygame.K_p:
                        self.stats.help_needed = False
                        self.stats.reset_stats()
                        self.stats.game_active = True
                        self.sb.prep_score()
                        self.zombies.empty()
                        self.poops.empty()
                        self._create_fleet()
                        self.panda.center_panda()


    def _check_keyup_events(self, event):
                     if event.key == pygame.K_RIGHT:
                          self.panda.moving_right = False
                     elif event.key == pygame.K_LEFT:
                          self.panda.moving_left = False

    def _check_play_button(self, mouse_pos):
          if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active :
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.zombies.empty()
            self.poops.empty()
            self._create_fleet()
            self.panda.center_panda()
                    
    def _check_question_button(self, mouse_pos):
          if self.question_button.rect.collidepoint(mouse_pos) :
            self.stats.game_active = False
            self.stats.help_needed = True
     
    
    def _fire_poop(self):
                new_poop = Poop(self)
                self.poops.add(new_poop)
    
    def _create_fleet(self):        # creates a fleet of zombies
          zombie = Zombie(self)
          zombie_width, zombie_height = zombie.rect.size
          available_space_x = self.settings.screen_width - (2 * zombie_width)
          number_zombies_x = available_space_x // (2*zombie_width)

          panda_height = self.panda.rect.height # determine num of rows of zombies that can fit
          available_space_y = (self.settings.screen_height - (zombie_height) - (2*panda_height))
          number_rows = available_space_y // (2 * zombie_height)

          for row_number in range(number_rows):
            for zombie_number in range(number_zombies_x):
                self._create_zombie(zombie_number, row_number)
            
          self.zombies_left = number_rows*number_zombies_x
                
    def _create_zombie(self, zombie_number, row_number):
                    zombie = Zombie(self)
                    zombie_width, zombie_height = zombie.rect.size
                    zombie.x = zombie_width + 2 * zombie_width * zombie_number
                    zombie.rect.x = zombie.x
                    zombie.rect.y = self.settings.screen_height - (zombie_height + 2 * zombie.rect.height * row_number)
                    self.zombies.add(zombie)

    def _update_zombies(self):
          self._check_fleet_edges()
          self.zombies.update()
          if pygame.sprite.spritecollideany(self.panda, self.zombies):
                self._panda_hit()
          self._check_zombies_bottom()

    def _update_poops(self):
        self.poops.update() # update poop positions

        for poop in self.poops.copy():    
              if poop.rect.bottom <= 0:
                    self.poops.remove(poop)

        collisions = pygame.sprite.groupcollide(self.poops, self.zombies, True, True) # checking for poops that have hit
                                                                  # zombies & to delete the poop and zombie that's been hit
        if collisions:
              for zombies in collisions.values():
                        self.stats.score += self.settings.zombie_points * len(zombies)
              pygame.mixer.music.load('images/dead.wav')
              pygame.mixer.music.play(0)
              self.zombies_left -= len(zombies)
              if self.zombies_left == 0:
                    self.stats.game_over = True
                    self.stats.win = True
                    self._update_screen()
                    sleep(5.0)
                    self.stats.game_active = False
                    self.stats.game_over = False
                    self._update_screen()
              self.sb.prep_score()
              self.sb.check_high_score()

    def _check_fleet_edges(self):   
          for zombie in self.zombies.sprites():
            if zombie.check_edges():
                self._change_fleet_direction()
                break
 
    def _change_fleet_direction(self):    # makes the fleet move in the other direction when it hits a side
          for zombie in self.zombies.sprites():
                zombie.rect.y -= self.settings.fleet_drop_speed
          self.settings.fleet_direction *= -1


    def _check_zombies_bottom(self):      # checks to see if the zombies have made it to the top of the screen
          screen_rect = self.screen.get_rect()
          for zombie in self.zombies.sprites():
                if zombie.rect.bottom <= screen_rect.top:
                     self._panda_hit()
                     break
                
    def _panda_hit(self):
      if self.stats.pandas_left > 2:
          self.stats.pandas_left -= 1
          self.sb.prep_lives()
          self.sb.show_score()
          pygame.mixer.music.load('images/hit.wav')
          pygame.mixer.music.play(0)

          self.zombies.empty()
          self.poops.empty()

          self._create_fleet()
          self.panda.center_panda()

          sleep(0.5)    # pauses game for half a second once hit occurs before resetting
      else:
             self.stats.game_over = False
             self.stats.game_active = False
             self._update_screen()
            

    def _update_screen(self):
         self.screen.fill(self.settings.bg_color)
         self.panda.blitme()
         for poop in self.poops.sprites():
               poop.draw_poop()
         self.zombies.draw(self.screen)
         self.sb.show_score()
         

         self.question_button.draw_button()
         if not self.stats.game_active and not self.stats.game_over:
              self.play_button.draw_button()
         elif self.stats.game_over and not self.stats.win:
               self.over_button.draw_button()
         elif self.stats.game_over and self.stats.win:
               self.win_button.draw_button()
         elif self.stats.help_needed:
               self.help_button.draw_button()
         pygame.display.flip() # draws empty screen after each iteration of while loop

    
if __name__ == '__main__':
    ai = ZombieInvasion()
    ai.run_game()
