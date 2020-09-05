import os
import pygame
import Important
from os import path

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

size = windowWidth, windowHeight = 800, 600
screen = pygame.display.set_mode(size)
sprites_dir = path.join(path.dirname(__file__), 'sprites')
bgImage = pygame.image.load(path.join(sprites_dir, 'mainMenu3.bmp'))
pygame.display.set_caption("Return to Eden")
pygame.display.set_icon(pygame.image.load(path.join(sprites_dir, 'playerShip64_right.gif')))

# kleuren
color_white = [255, 255, 255]
color_black = [0, 0, 0]
color_red = [255, 0, 0]
color_green = [0, 255, 0]
color_blue = [0, 0, 255]
color_sun = [255, 255, 44]

FPS = pygame.time.Clock()


jupiter_done = False
venus_done = False
mars_done = False
uranus_done = False
saturnus_done = False
neptunus_done = False
game_completed = False


def quitmaingame():
    global game_completed
    text_font = pygame.font.SysFont("algerian", 20)

    def complete():
        aarde = pygame.image.load(path.join(sprites_dir, 'Earth3.png'))
        aarde = pygame.transform.scale(aarde, (1000, 550))
        screen.fill(color_black)
        screen.blit(aarde, (0, 0))
        msg1, msg2 = "Thank you for playing Return to EDEN", "Main menu made by Menno & Hakan"
        msg3, msg4 = "Jupiter made by Menno", "Venus made by Julia"
        msg5, msg6 = "Mars made by Hakan", "Saturnus made by Erik"
        msg7, msg8 = "Uranus made by Dines", "Neptunus made by Thomas"

        text_s, text_r = Important.text_objects(msg1, text_font, color_white)
        text_r.left, text_r.top = 20, 30
        text_s1, text_r1 = Important.text_objects(msg2, text_font, color_white)
        text_r1.left, text_r1.top = 20, 60
        text_s2, text_r2 = Important.text_objects(msg3, text_font, color_white)
        text_r2.left, text_r2.top = 20, 90
        text_s3, text_r3 = Important.text_objects(msg4, text_font, color_white)
        text_r3.left, text_r3.top = 20, 120
        text_s4, text_r4 = Important.text_objects(msg5, text_font, color_white)
        text_r4.left, text_r4.top = 20, 150
        text_s5, text_r5 = Important.text_objects(msg6, text_font, color_white)
        text_r5.left, text_r5.top = 20, 180
        text_s6, text_r6 = Important.text_objects(msg7, text_font, color_white)
        text_r6.left, text_r6.top = 20, 210
        text_s7, text_r7 = Important.text_objects(msg8, text_font, color_white)
        text_r7.left, text_r7.top = 20, 240

        screen.blit(text_s, text_r), screen.blit(text_s1, text_r1), screen.blit(text_s2, text_r2)
        screen.blit(text_s3, text_r3), screen.blit(text_s4, text_r4), screen.blit(text_s5, text_r5)
        screen.blit(text_s6, text_r6), screen.blit(text_s7, text_r7)

    def notcomplete():
        bg = pygame.image.load(path.join(sprites_dir, 'exploding planet.png'))
        screen.fill(color_black)
        screen.blit(bg, (0, 0))
        msg1 = "As you were returning from a planet you could see an explosion."
        msg2 = "It came from Earth..."
        msg3 = "After all the setback and watching earth beïng destroyed,"
        msg4 = "You didn't see any meaning left in living."
        msg5 = "So you opened the door of your spaceship, and went for a long walk."

        text_s, text_r = Important.text_objects(msg1, text_font, color_white)
        text_r.center = (windowWidth/2, 40)
        text_s1, text_r1 = Important.text_objects(msg2, text_font, color_white)
        text_r1.center = (windowWidth/2, 80)
        text_s2, text_r2 = Important.text_objects(msg3, text_font, color_white)
        text_r2.center = (windowWidth/2, 120)
        text_s3, text_r3 = Important.text_objects(msg4, text_font, color_white)
        text_r3.center = (windowWidth/2, 460)
        text_s4, text_r4 = Important.text_objects(msg5, text_font, color_white)
        text_r4.center = (windowWidth/2, 500)

        screen.blit(text_s, text_r), screen.blit(text_s1, text_r1)
        screen.blit(text_s2, text_r2), screen.blit(text_s3, text_r3)
        screen.blit(text_s4, text_r4)

    if game_completed:
        complete()
    else:
        notcomplete()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        Important.button("Quit", 350, 560, 100, 30, color_red, color_white, screen, color_black, quit)
        pygame.display.update()
        FPS.tick(15)


def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitmaingame()

        # werken aan knoppen uncomment dit:
        # screen.blit(bgImage, (0, 0))

        Important.button("Jupiter", 90, 370, 160, 160, color_green, color_white, screen, color_black, game_jupiter)
        Important.button("Venus", 620, 380, 120, 120, color_green, color_white, screen, color_black, game_venus)
        Important.button("Mars", 365, 25, 85, 85, color_green, color_white, screen, color_black, game_mars)
        Important.button("Saturnus", 280, 225, 100, 100, color_green, color_white, screen, color_black, game_saturnus)
        Important.button("Neptunus", 400, 425, 140, 140, color_green, color_white, screen, color_black, game_neptunus)
        Important.button("Uranus", 560, 210, 110, 110, color_green, color_white, screen, color_black, game_uranus)

        Important.button("Earth", 30, 20, 115, 115, color_blue, color_red, screen, color_black, game_earth)
        Important.button("Sun", 625, 10, 170, 170, color_blue, color_white, screen, color_black, quitmaingame)

        # werken aan knoppen? comment dit:
        screen.blit(bgImage, (0, 0))
        pygame.display.update()
        FPS.tick(15)


def game_earth():
    pygame.mixer.music.stop()
    global jupiter_done
    global venus_done
    global mars_done
    global uranus_done
    global saturnus_done
    global neptunus_done
    global game_completed

    from Jupiter_Folder.Jupiter_Ascending import jupiter_game_completed
    jupiter_done = jupiter_game_completed

    from Mars_Folder.MarsGame import mars_game_completed
    mars_done = mars_game_completed

    from Venus_Folder.Jumping_off_Venus import venus_game_completed
    venus_done = venus_game_completed

    from Uranus_Folder.MemoryGame import uranus_game_completed
    uranus_done = uranus_game_completed

    from Saturnus_folder.minigame_meteor_rush import saturnus_game_completed
    saturnus_done = saturnus_game_completed

    from Neptunus_Folder.FuelFlight import neptune_game_completed
    neptunus_done = neptune_game_completed

    small_text = pygame.font.SysFont("algerian", 20)
    # om snel het eindscherm te testen
    # if True:
    if jupiter_done and venus_done and mars_done and uranus_done and saturnus_done and neptunus_done:
        bg = pygame.image.load(path.join(sprites_dir, 'Earth3.png'))
        bg = pygame.transform.scale(bg, (1000, 550))
        sc = pygame.image.load(path.join(sprites_dir, 'playerShip64_right.gif'))
        sc = pygame.transform.scale(sc, (100, 100))
        game_completed = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitmaingame()
            screen.fill(color_black)
            screen.blit(bg, (0, 0))
            screen.blit(sc, (50, 350))
            # small_text = pygame.font.SysFont("algerian", 25)
            color_fin = [200, 120, 100]
            text_s, text_r = Important.text_objects("After countless dangerous situations you made it to Earth.", small_text, color_fin)
            text_r.left, text_r.top = 20, 20
            text_s1, text_r1 = Important.text_objects("You have finally found peace.", small_text, color_fin)
            text_r1.left, text_r1.top = 20, 40
            text_s2, text_r2 = Important.text_objects("Or so you thought...", small_text, color_fin)
            text_r2.left, text_r2.top = 20, 60

            screen.blit(text_s, text_r), screen.blit(text_s1, text_r1), screen.blit(text_s2, text_r2)

            Important.button("Keep playing", 250, 560, 120, 30, color_green, color_white, screen, color_black, main_menu)
            Important.button("Quit", 450, 560, 120, 30, color_red, color_white, screen, color_black, quitmaingame)
            pygame.display.update()
            FPS.tick(15)
    else:

        bg = pygame.image.load(path.join(sprites_dir, 'Earth_far2.png'))
        bg = pygame.transform.scale(bg, (1422, 800))
        lijst = []
        lijst_image = pygame.image.load(path.join(sprites_dir, 'Fuel.png'))
        lijst_image = pygame.transform.scale(lijst_image, (50, 50))
        planets = ""
        if not jupiter_done:
            planets = planets + " Jupiter "
        else:
            lijst.append(lijst_image)
        if not venus_done:
            planets = planets + " Venus "
        else:
            lijst.append(lijst_image)
        if not mars_done:
            planets = planets + " Mars "
        else:
            lijst.append(lijst_image)
        if not uranus_done:
            planets = planets + " Uranus "
        else:
            lijst.append(lijst_image)
        if not saturnus_done:
            planets = planets + " Saturnus "
        else:
            lijst.append(lijst_image)
        if not neptunus_done:
            planets = planets + " Neptunus "
        else:
            lijst.append(lijst_image)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_menu()

            screen.fill(color_black)
            screen.blit(bg, (-200, -100))
            # small_text = pygame.font.SysFont("algerian", 25)
            text1 = "You still have to go to the following planets for fuel: "
            text_s, text_r = Important.text_objects(text1, small_text, color_white)
            text_r.left, text_r.top = 30, 40
            text_s1, text_r1 = Important.text_objects(planets, small_text, color_white)
            text_r1.left, text_r1.top = 30, 80
            text_s2, text_r2 = Important.text_objects("Fuel:", small_text, color_white)
            text_r2.left, text_r2.top = 30, 520

            screen.blit(text_s, text_r), screen.blit(text_s1, text_r1), screen.blit(text_s2, text_r2)
            pos = 100
            for l in lijst:
                screen.blit(l, (pos, 500))
                pos += 50
            # screen.blit(lijst, (50, 500))
            Important.button("Return", 350, 370, 100, 50, color_green, color_white, screen, color_black, main_menu)
            pygame.display.update()
            FPS.tick(15)


def game_saturnus():
    from Saturnus_folder import minigame_meteor_rush
    minigame_meteor_rush.mini_game()


def game_neptunus():
    from Neptunus_Folder import FuelFlight
    FuelFlight.show_go_screen()


def game_uranus():
    from Uranus_Folder import MemoryGame
    MemoryGame.menno()


def game_jupiter():
    from Jupiter_Folder import Jupiter_Ascending
    Jupiter_Ascending.game_intro()


def game_venus():
    from Venus_Folder import Jumping_off_Venus
    Jumping_off_Venus.intro()


def game_mars():
    def start():
        from Mars_Folder import MarsGame
        MarsGame.hisGame()

    def stop():
        main_menu()

    screen.fill(color_black)
    small_text = pygame.font.SysFont("algerian", 15)
    large_text = pygame.font.SysFont("algerian", 35, bold=True)
    text_s, text_r = Important.text_objects("Maze Shipper", large_text, color_white)
    text_r.center = (windowWidth/2, 50)
    text_s1, text_r1 = Important.text_objects("Get to the end point while avoiding the enemies!", small_text, color_white)
    text_r1.center = (windowWidth/2, 150)
    text_s2, text_r2 = Important.text_objects("Move with the arrow keys.", small_text, color_white)
    text_r2.center = (windowWidth/2, 200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop()
        Important.button("Start", 250, 350, 100, 50, color_green, color_white, screen, color_black, start)
        Important.button("Quit", 450, 350, 100, 50, color_red, color_white, screen, color_black, stop)

        screen.blit(text_s, text_r), screen.blit(text_s1, text_r1), screen.blit(text_s2, text_r2)
        pygame.display.flip()


    # pygame.init()
    # pygame.display.quit()
    # pygame.quit()
    # pygame.display.iconify()
