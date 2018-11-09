class Settings():
    """A class to store all settings for meme invasion"""

    def __init__(self):
        """Initialize the games settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (224, 224, 224) #RGB

        #pepe settings
        self.pepe_speed_factor = 1.5
        self.pepe_limit = 3

        #bullet setting
        self.bullet_speed_factor = 3
        self.bullet_width = 20
        self.bullet_height = 5
        self.bullet_color = 255, 0, 0 #RGB
        self.bullets_allowed = 3

        #meme settings
        self.meme_speed_factor = 1
        self.fleet_drop_speed = 20

        #how quickly the game speeds up
        self.speedup_scale = 1.2

        #how quickly the meme point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.pepe_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.meme_speed_factor = 1

        # fleet_direction of 1 represents down; -1 represents up
        self.fleet_direction = 1

        #scoreing
        self.meme_points = 100

    def increase_speed(self):
        """increase speed settings and meme point values"""
        self.pepe_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.meme_speed_factor *= self.speedup_scale

        self.meme_points = int(self.meme_points * self.score_scale)

        print(self.meme_points)