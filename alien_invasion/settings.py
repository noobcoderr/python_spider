class Settings():
    """a class that store all settings of the Alien invasion"""

    def __init__(self):
        """init settings of the game"""
        #set screen
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (230,230,230)

        # sheep of the ship
        self.ship_speed_factor = 1.5

        #settings of bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height =15
        self.bullet_color = 60,60,60