import pygame
import os
import sys
import Important
from os import path


os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

size = windowWidth, windowHeight = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Return to Eden")
if getattr(sys, 'frozen', False):
    # frozen (EXE)      # verwijst nu naar het exe bestand, maar moet naar een map naast het exe bestand wijzen
    exe_dir = os.path.dirname(sys.executable)
    lib_dir = path.join(exe_dir, 'lib')
    sprites_dir = path.join(lib_dir, 'sprites')
    # sprites_dir = path.join(sprites_dir, 'sprites')
else:
    # unfrozen (nonEXE)
    sprites_dir = path.join(path.dirname(__file__), 'sprites')
pygame.display.set_icon(pygame.image.load(path.join(sprites_dir, 'playerShip64_right.gif')))

# kleuren
color_white = [255, 255, 255]
color_black = [0, 0, 0]
color_red = [255, 0, 0]
color_green = [0, 255, 0]
color_blue = [0, 0, 255]
color_sun = [232, 182, 17]

FPS = pygame.time.Clock()


def main_intro():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(color_black)
        # text formaat aangeven
        small_text = pygame.font.SysFont("algerian", 15)
        large_text = pygame.font.SysFont("algerian", 35, bold=True)

        # het verhaal
        text_s, text_r = Important.text_objects("Return to EDEN", large_text, color_white)
        text_r.center = (windowWidth/2, 50)
        text_s1, text_r1 = Important.text_objects("During the intergalactic war of 2529 you lost most of your friends.", small_text, color_white)
        text_r1.center = (windowWidth/2, 100)
        text_s2, text_r2 = Important.text_objects("After the war you decided it was time to go back home, back to earth.", small_text, color_white)
        text_r2.center = (windowWidth/2, 150)
        text_s3, text_r3 = Important.text_objects("As you were travelling through the galaxy you noticed you were almost out of fuel.", small_text, color_white)
        text_r3.center = (windowWidth/2, 200)
        text_s4, text_r4 = Important.text_objects("Your scanners show that there is fuel on the other planets in the milkyway.", small_text, color_white)
        text_r4.center = (windowWidth/2, 250)
        text_s7, text_r7 = Important.text_objects("To get enough fuel to make it to earth, you will have to stop at every planet.", small_text, color_white)
        text_r7.center = (windowWidth/2, 300)
        text_s5, text_r5 = Important.text_objects("Each planet requires a different method to get to the fuel.", small_text, color_white)
        text_r5.center = (windowWidth/2, 350)
        text_s6, text_r6 = Important.text_objects("You know you don't have any other chance. You want to get home as quick as possible.", small_text, color_white)
        text_r6.center = (windowWidth/2, 400)
        text_s8, text_r8 = Important.text_objects("Danger: The sun is too hot for the shield of your spaceship. Stay away from the sun!", small_text, color_sun)
        text_r8.center = (windowWidth/2, 450)

        # knoppen om het spel te beginnen/sluiten
        Important.button("Start", 250, 500, 100, 50, color_green, color_white, screen, color_black, hoofdmenu)
        Important.button("Quit", 450, 500, 100, 50, color_red, color_white, screen, color_black, quit_intro)

        # text naar het scherm schrijven
        screen.blit(text_s, text_r), screen.blit(text_s1, text_r1), screen.blit(text_s2, text_r2)
        screen.blit(text_s3, text_r3), screen.blit(text_s4, text_r4), screen.blit(text_s5, text_r5)
        screen.blit(text_s6, text_r6), screen.blit(text_s7, text_r7), screen.blit(text_s8, text_r8)

        # scherm updaten
        pygame.display.update()
        FPS.tick(15)


def hoofdmenu():
    import MainMenuV4
    MainMenuV4.main_menu()


def quit_intro():
    pygame.quit()
    quit()


main_intro()
