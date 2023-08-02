class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        self.help_needed = False
        self.game_over = False

    def reset_stats(self):
        self.pandas_left = self.settings.panda_limit
        self.score = 0
