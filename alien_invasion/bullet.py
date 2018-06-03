import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """a class that manage how a ship fire"""

    def __init__(self,ai_settings,screen,ship):
        """create a bullet where ship at"""
        super(Bullet,self).__init__()
        self.screen = screen

        #creat a bullet rectangle at (0,0) then set right location
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store location of bullet that expression with float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move up the bullet"""
        #update the value of the bullet location
        self.y -= self.speed_factor
        #update the vale of bullet rect
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
