import pygame
import game_functions as gf

from settings import Settings
from pepe import Pepe
from pygame.sprite import Group
from meme import Meme
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Meme_Invaders')

    #make the play button
    play_button = Button(ai_settings, screen, "Play Meme_Invaders")

    #create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #make a meme
    meme = Meme(ai_settings, screen)

    #make a pepe
    pepe = Pepe(ai_settings, screen)

    #make a group of bullets and memes
    bullets = Group()
    memes = Group()

    #create the fleet of memes
    gf.create_fleet(ai_settings, screen, pepe, memes)

    #start main loop of the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, pepe, memes, bullets)

        if stats.game_active:
            pepe.update()
            gf.update_bullets(ai_settings, screen, stats, sb, pepe, memes, bullets)
            gf.update_memes(ai_settings, screen, stats, sb, pepe, memes, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, pepe, memes, bullets, play_button)

run_game()
