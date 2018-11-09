import sys

import pygame
from bullet import Bullet
from settings import Settings
from meme import Meme
from time import sleep

def check_keydown_events(event, ai_settings, screen, pepe, bullets):
    """responds to key pushes"""
    if event.key == pygame.K_RIGHT:
        pepe.moving_right = True
    elif event.key == pygame.K_LEFT:
        pepe.moving_left = True
    elif event.key == pygame.K_UP:
        pepe.moving_up = True
    elif event.key == pygame.K_DOWN:
        pepe.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, pepe, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, pepe, bullets):
    """fire a bullet if limit not reached yet"""
    #create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, pepe)
        bullets.add(new_bullet)

def update_bullets(ai_settings, screen, stats, sb, pepe, memes, bullets):
    """update position of bullets and get rid of old bullets"""
    #update bullet positions
    bullets.update()

    #get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.right >= Settings().screen_width:
            bullets.remove(bullet)

    check_bullet_meme_collisions(ai_settings, screen, stats, sb, pepe, memes, bullets)

def check_bullet_meme_collisions(ai_settings, screen, stats, sb, pepe, memes, bullets):
    """responds to bullet-meme collisions"""
    #remove any bullets and memes that have collided
    collisions = pygame.sprite.groupcollide(bullets, memes, True, True)

    if collisions:
        for memes in collisions.values():
            stats.score += ai_settings.meme_points * len(memes)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(memes) == 0:
        #if the entire fleet is setroyed, start a new level
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, pepe, memes)

        #increase level
        stats.level += 1
        sb.prep_level()


def check_keyup_events(event, pepe):
    """responds to key releases"""
    if event.key == pygame.K_RIGHT:
        pepe.moving_right = False
    elif event.key == pygame.K_LEFT:
        pepe.moving_left = False
    elif event.key == pygame.K_UP:
        pepe.moving_up = False
    elif event.key == pygame.K_DOWN:
        pepe.moving_down = False

def check_events(ai_settings, screen, stats, sb, play_button, pepe, memes, bullets):
    """responds to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, pepe, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, pepe)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, pepe, memes, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button,
                      pepe, memes, bullets, mouse_x, mouse_y):
    """starts a new game when the player clicks play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #reset the game settings
        ai_settings.initialize_dynamic_settings()

        #hide the mouse cursor
        pygame.mouse.set_visible(False)

        #resets the game stats
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_pepes()

        #empty the list of memes and bullets
        memes.empty()
        bullets.empty()

        #create a new fleet and center the ship
        create_fleet(ai_settings, screen, pepe, memes)
        pepe.center_pepe()

def update_screen(ai_settings, screen, stats, sb, pepe, memes, bullets, play_button):
    """update images on the screen and flip to the new screen"""
    #redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)



    #redraw all the bullets behind pepe and memes
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pepe.blitme()
    memes.draw(screen)

    #draw score info
    sb.show_score()

    #draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    #make the most recently drawn screen visible
    pygame.display.flip()

def get_number_memes_y(ai_settings, meme_height):
    #determine the number of memes that fit in a row
    available_space_y = ai_settings.screen_height - 2 * meme_height
    number_memes_y = int(available_space_y / (2 * meme_height))
    return number_memes_y

def get_number_columns(ai_settings, pepe_width, meme_width):
    """determine the number of rows of memes that fit in the screen"""
    available_space_y = (ai_settings.screen_width -
        (3 * meme_width) - pepe_width)
    number_columns = int(available_space_y / (2 * meme_width) - 1)
    return number_columns

def create_meme(ai_settings, screen, memes, meme_number, column_number):
    """create a meme and place it in the row"""
    meme = Meme(ai_settings, screen)
    meme_height = meme.rect.height
    meme.rect.x = (meme.rect.width + 300) + 2 * meme.rect.height * column_number
    meme.y = meme_height + 2 * meme_height * meme_number

    meme.rect.y = meme.y
    memes.add(meme)

def create_fleet(ai_settings, screen, pepe, memes):
    """create a full fleet of meme"""
    # create a meme and find the number of memes in a row
    # spacing between each meme is equal to one meme width
    meme = Meme(ai_settings, screen)
    number_memes_y = get_number_memes_y(ai_settings, meme.rect.height)
    number_columns = get_number_columns(ai_settings, pepe.rect.width, meme.rect.width)

    #create fleet of memes
    for column_number in range(number_columns):
        for meme_number in range(number_memes_y ):
            create_meme(ai_settings, screen, memes, meme_number, column_number)

def check_fleet_edges(ai_settings, memes):
    """respond appropriately if any meme have reached an edge"""
    for meme in memes.sprites():
        if meme.check_edges():
            change_fleet_direction(ai_settings, memes)
            break

def change_fleet_direction(ai_settings, memes):
    """drop the entire fleet and change the fleets direction"""
    for meme in memes.sprites():
        meme.rect.x -= ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def pepe_hit(ai_settings, screen, stats, sb, pepe, memes, bullets):
    """responds to pepe being hit by meme"""
    if stats.pepes_left > 0:

        # subtracts 1 from pepes_left
        stats.pepes_left -= 1

        #update scoreboard
        sb.prep_pepes()

        #empty the list of memes and bullets
        memes.empty()
        bullets.empty()

        #create a new fleet and center the pepe
        create_fleet(ai_settings, screen, pepe, memes)
        pepe.center_pepe()

        #pause
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_memes_left(ai_settings, screen, stats, sb, pepe, memes, bullets):
    """check if any memes have reached the left of the screen"""
    screen_rect = screen.get_rect()
    for meme in memes.sprites():
        if meme.rect.left <= screen_rect.left:
            pepe_hit(ai_settings, screen, stats, sb, pepe, memes, bullets)
            break

def update_memes(ai_settings, screen, stats, sb, pepe, memes, bullets):
    """
    check if the fleet is at an edge,
    and then update the postions of all memes in the fleet.
    """
    check_fleet_edges(ai_settings, memes)
    memes.update()

    #look for meme-pepe collisions
    if pygame.sprite.spritecollideany(pepe, memes):
        pepe_hit(ai_settings, screen, stats, sb, pepe, memes, bullets)

    #look for memes hitting the left of the screen
    check_memes_left(ai_settings, screen, stats, sb, pepe, memes, bullets)

def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
