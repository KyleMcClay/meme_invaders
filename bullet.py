import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the pepe"""

    def __init__(self, ai_settings, screen, pepe):
        """create a bullet object at the pepes current position"""
        super().__init__()
        self.screen = screen

        #create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centery = pepe.rect.centery
        self.rect.right = pepe.rect.right

        #Store the bullets position as a decimal value.
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move the bullet up the screen"""
        #update the decimal position of the bullet
        self.x += self.speed_factor
        #update the rect position
        self.rect.x = self.x

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

