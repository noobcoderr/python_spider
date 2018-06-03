import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        """init ship and set its start location"""
        self.screen = screen
        self.ai_settings = ai_settings

        #load ship pic and get its bounding rectangle(wai jie juxing)
        self.image = pygame.image.load('images/shipbmp.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #let each ship located at the bottom of the central
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store float value in attribute-center
        self.center = float(self.rect.centerx)
        #move sign
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False



    def update(self):
        """adjust location of the ship by move sign"""
        # update the value of center not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1

        #update rect value by self.center
        self.rect.centerx = self.center


    def blitme(self):
        """draw ship on designated spot"""
        self.screen.blit(self.image,self.rect)

