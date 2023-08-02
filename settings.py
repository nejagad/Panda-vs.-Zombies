class Settings:

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (32, 42, 68)
      #  self.panda_speed = 1.5

       # self.poop_speed = 1.0
        self.poop_width = 3
        self.poop_height = 15
        self.poop_color = (139,69,19)

      #  self.zombie_speed = 1.0
        self.fleet_drop_speed = 10
     #   self.fleet_direction = 1
        self.panda_limit = 3

        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
            self.panda_speed = 1.5
            self.poop_speed = 3.0
            self.zombie_speed = 1.0
            self.fleet_direction = 1
            self.zombie_points = 10

    def increase_speed(self):
            self.panda_speed *= self.speedup_scale
            self.poop_speed *= self.speedup_scale
            self.zombie_speed *= self.speedup_scale
