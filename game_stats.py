class GameStats():
    """track statistics for meme invasion"""

    def __init__ (self, ai_settings):
        """initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #start meme invasion in an active state
        self.game_active = True

        #start game in an inactive state
        self.game_active = False

        #high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """initialize stats that can change during the game"""
        self.pepes_left = self.ai_settings.pepe_limit
        self.score = 0
        self.level = 1