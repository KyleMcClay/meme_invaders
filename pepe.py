import pygame
from pygame.sprite import Sprite

class Pepe(Sprite):

    def __init__(self, ai_settings, screen):
        """initialize the ship and set its starting position"""
        super(Pepe,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the pepe image and get its rect
        self.image = pygame.image.load('images\pepe 60by60.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new pepe at the left center of the screen.
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        #store a decimal value for the pepes center
        self.center = float(self.rect.centerx)
        self.center1 = float(self.rect.centery)

        #movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #ship settings
        self.pepe_speed_factor = 1.5

    def update(self):
        """update pepes position"""
        #update the ships center value, not the rect
        ###coordinates y = 0 is the top of the screen y = 1000000 is bottom of screen
        ###coordinates x = 0 is far left
        if self.moving_right and self.rect.right < self.screen_rect.right * (1/4):
            self.center += self.ai_settings.pepe_speed_factor
        if self.moving_left and self.rect.left > (self.screen_rect.right) * (0): ### 0 gives ship all of x
            self.center -= self.ai_settings.pepe_speed_factor
        if self.moving_up and self.rect.top > (self.screen_rect.bottom)*(0): ### 0 gives ship all of y
            self.center1 -= self.ai_settings.pepe_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center1 += self.ai_settings.pepe_speed_factor

        #update rect object from self.center.
        self.rect.centerx = self.center
        self.rect.centery = self.center1

    def blitme(self):
        """Draw the pepe at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_pepe(self):
        """center the ship on the screen"""
        self.center = self.screen_rect.left + 30
