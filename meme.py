import pygame
import random
from pygame.sprite import Sprite
from settings import Settings

class Meme(Sprite):
    """a class to represent a single meme in the meme fleet"""
    def __init__(self, ai_settings, screen):
        """initialize the meme and set its starting position"""
        super(Meme, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #a list of meme images
        list_meme = []

        list_meme.append('image meme villians\harambe.bmp')
        list_meme.append('image meme villians\doge deal with it.jpg')
        list_meme.append('image meme villians\grumpy cat.jpg')
        list_meme.append('image meme villians/Overly Attached Girlfriend.png')
        list_meme.append('image meme villians/mah heart mah sole.png')
        list_meme.append('image meme villians/TrollFace.jpg')
        list_meme.append('image meme villians/seal.jpg')
        list_meme.append('image meme villians/Y-U-No.jpg')
        list_meme.append('image meme villians/Good Guy Greg.jpg')
        list_meme.append('image meme villians/10 Guy.jpg')
        list_meme.append('image meme villians/mother of god.jpg')
        list_meme.append('image meme villians/nyan-cat-01-625x450.jpg')
        list_meme.append('image meme villians/First World Problems.jpg')
        list_meme.append('image meme villians/Matrix Morpheus.jpg')
        list_meme.append('image meme villians/business-cat-6a42c946fec8c3cd45824ae87dbef0804a7ffee6b7c44d64e27e38cf9622b13c.jpg')
        list_meme.append('image meme villians/Success Kid.jpg')
        list_meme.append("image meme villians/Kermit the Frog - But That's None Of My Business.jpg")
        list_meme.append("image meme villians/drunk college kid.jpg")
        list_meme.append("image meme villians/Roll-Safe-Think-About-It.jpg")
        list_meme.append("image meme villians/black science guy.png")
        list_meme.append("image meme villians/raptor.jpg")
        list_meme.append("image meme villians/American Eagle.jpg")
        list_meme.append("image meme villians/Condescending Wonka.jpg")
        list_meme.append("image meme villians/Bad Luck Brian.jpg")
        list_meme.append("image meme villians/Forever Alone.jpg")
        list_meme.append("image meme villians/Imminent Ned Brace Yourselves.jpg")
        list_meme.append("image meme villians/Conspiracy Keanu.jpg")
        list_meme.append("image meme villians/Archer Ants.jpg")
        list_meme.append("image meme villians/most_interesting.jpg")
        list_meme.append("image meme villians/me seeks.png")
        list_meme.append("image meme villians/rick and morty.jpg")

        #load the meme and set its rect attribute

        self.image = pygame.image.load(list_meme[random.randint(0 , 30)])
        self.rect = self.image.get_rect()

        #start each new meme near the bottom right of the screen
        self.rect.x = (Settings().screen_width) - 120
        self.rect.y = (Settings().screen_height) - 120


        #store the memes exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the meme at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """return True if meme is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True

    def update(self):
        """move meme up or down"""
        self.y += (self.ai_settings.meme_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.y = self.y

