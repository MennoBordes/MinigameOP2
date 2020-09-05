import pygame as pg
import random
import os
from pygame import *
from random import randint
from os import path
import Important

os.environ["SDL_VIDEO_CENTERED"] = "1"
pg.init()
clock = pg.time.Clock()
afbeeldingen_dir = path.join(path.dirname(__file__), 'afbeeldingen')
muziek_dir = path.join(path.dirname(__file__), 'muziek')

# init display
size = width, height = 800, 600
screen = pg.display.set_mode(size)
# pg.display.set_caption("Jumping off venus")
background = pg.image.load(path.join(afbeeldingen_dir, 'venusss.jpg'))
image = pg.image.load(path.join(afbeeldingen_dir, 'playerShip64.GIF'))
rotated_image = pg.transform.rotate(image, 180)
lava = pg.image.load(path.join(afbeeldingen_dir, 'lava.jpg'))

# init figure
player_width = 40
player_height = 40
jump = height // 6
minimum_platforms = 7
platforms = [{'rect': pg.Rect(0, height - 30, width, 30), 'velocity': 1},
             {'rect': pg.Rect(random.randint(0, width - 200), 470, 200, 5), 'velocity': 1},
             {'rect': pg.Rect(random.randint(0, width - 200), 370, 200, 5), 'velocity': 1},
             {'rect': pg.Rect(random.randint(0, width - 200), 270, 200, 5), 'velocity': 1},
             {'rect': pg.Rect(random.randint(0, width - 200), 170, 200, 5), 'velocity': 1},
             {'rect': pg.Rect(random.randint(0, width - 200), 70, 200, 5), 'velocity': 1}]

isJumping = True
goingDown = False
currentYPosition = height - 70
hit = False
play = False
begin = False
movement_speed = 5
green = [0, 204, 0]
red = [225, 0, 0]
black = [0, 0, 0]
white = (225, 225, 225)
blue = [0, 0, 225]
green_button = [0, 150, 0]
red_button = [150, 0, 0]
paused = False
venus_game_completed = False


def win_game():
    global venus_game_completed
    mixer.init()
    mixer.music.load(path.join(muziek_dir, 'ScareCrow_-_Last_Action_Hero_-_Level_2_-_Straight_Mix.mp3'))
    mixer.music.play(-1, 0)
    venus_game_completed = True

    while win_game:
        textcolor = [200, 200, 200]
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game()
        screen.fill((0, 0, 0))
        small_text = pg.font.SysFont("algerian", 20)
        large_text = pg.font.SysFont("algerian", 35, bold=True)
        text_surf1, text_rect1 = Important.text_objects("You won!!!", large_text, textcolor)
        text_rect1.center = (width/2, height/2/3.5)

        text_surf2, text_rect2 = Important.text_objects("You're fast enough", small_text, textcolor)
        text_rect2.center = (width/2, height/2/2)

        text_surf3, text_rect3 = Important.text_objects("Good job, you earn the fuel", small_text, textcolor)
        text_rect3.center = (width/2, height/2/1.5)

        text_surf4, text_rect4 = Important.text_objects("Try this game again or go to the next planet", small_text, textcolor)
        text_rect4.center = (width/2, height/2/1.2)

        # schrijf naar het scherm
        screen.blit(text_surf1, text_rect1)
        screen.blit(text_surf2, text_rect2)
        screen.blit(text_surf3, text_rect3)
        screen.blit(text_surf4, text_rect4)

        Important.button("Restart", 150, 500, 100, 50, green, green_button, screen, black, intro)
        Important.button("Quit", 550, 500, 100, 50, red, red_button, screen, black, quit_game)
        pg.display.flip()
        clock.tick(0)


def game_over():
    global timer
    global point
    score = timer.render("Score "+str(point)+" of the 650", 0, (225, 225, 225))

    mixer.init()
    mixer.music.load(path.join(muziek_dir, 'DAWilson_-_Turrican_II_Freedom_Blue_Sky_Mix.mp3'))
    mixer.music.play(-1, 0)

    while game_over:
        textcolor = [200, 200, 200]
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game()
        screen.fill((0, 0, 0))
        small_text = pg.font.SysFont("algerian", 20)
        large_text = pg.font.SysFont("algerian", 35, bold=True)
        text_surf1, text_rect1 = Important.text_objects("Game over", large_text, textcolor)
        text_rect1.center = (width/2, height/2/3.5)

        text_surf2, text_rect2 = Important.text_objects("You're too late...", small_text, textcolor)
        text_rect2.center = (width/2, height/2/2)

        text_surf3, text_rect3 = Important.text_objects("It was too hot for your spaceship and for you", small_text, textcolor)
        text_rect3.center = (width/2, height/2/1.5)

        text_surf4, text_rect4 = Important.text_objects("So you can try again or you die", small_text, textcolor)
        text_rect4.center = (width/2, height/2/1.2)

        # write to screen
        screen.blit(score, (350, 450))
        screen.blit(text_surf1, text_rect1)
        screen.blit(text_surf2, text_rect2)
        screen.blit(text_surf3, text_rect3)
        screen.blit(text_surf4, text_rect4)

        Important.button("Restart", 150, 500, 100, 50, green, green_button, screen, black, game_loop)
        Important.button("Quit", 550, 500, 100, 50, red, red_button, screen, black, quit_game)
        pg.display.flip()
        clock.tick(0)


def unpaused():
    global paused
    mixer.init()
    mixer.music.load(path.join(muziek_dir, 'Murdock_-_Stardust_Memories_MDK_remix.MP3'))
    mixer.music.play(-1, 0)
    paused = False


def pause():
    global timer
    global point
    score = timer.render("Score "+str(point)+" of the 650", 0, (225, 225, 225))
    mixer.init()
    mixer.music.load(path.join(muziek_dir, 'Peter_Gantar_-_Loveland_Mr_Oli.mp3'))
    mixer.music.play(-1, 0)

    while paused:
        textcolor = [200, 200, 200]
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game()

        screen.fill((0, 0, 0))
        small_text = pg.font.SysFont("algerian", 20)
        large_text = pg.font.SysFont("algerian", 35, bold=True)
        text_surf1, text_rect1 = Important.text_objects("Pause", large_text, textcolor)
        text_rect1.center = (width/2, height/2/3.5)

        text_surf2, text_rect2 = Important.text_objects("When you click on restart the game will go on", small_text, textcolor)
        text_rect2.center = (width/2, height/2/2)

        text_surf3, text_rect3 = Important.text_objects("When you click on Quit tis game will end", small_text, textcolor)
        text_rect3.center = (width/2, height/2/1.5)

        # schrijf naar het scherm
        screen.blit(score, (350, 450))
        screen.blit(text_surf1, text_rect1)
        screen.blit(text_surf2, text_rect2)
        screen.blit(text_surf3, text_rect3)

        Important.button("Continue", 150, 500, 100, 50, green, green_button, screen, black, unpaused)
        Important.button("Restart", 350, 500, 100, 50, green, green_button, screen, black, game_loop)
        Important.button("Quit", 550, 500, 100, 50, red, red_button, screen, black, quit_game)
        pg.display.flip()
        clock.tick(0)


def addplatform():
    np = {'rect': pg.Rect(random.randint(0, width - 200), 0, 200, 5)}
    k = platforms.append(np)
    return k


def quit_game():
    pg.mixer.music.stop()
    import MainMenuV4
    MainMenuV4.main_menu()


def intro():
    mixer.init()
    mixer.music.load(path.join(muziek_dir, 'DeAdLy_cOoKiE_-_Odyssey.mp3'))
    mixer.music.play(-1, 0)

    while True:
        textcolor = [200, 200, 200]
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game()
        screen.fill((0, 0, 0))
        small_text = pg.font.SysFont("algerian", 20)
        large_text = pg.font.SysFont("algerian", 35, bold=True)
        text_surf1, text_rect1 = Important.text_objects("Welcome to jumping off Venus", large_text, textcolor)
        text_rect1.center = (width/2, height/2/5)

        text_surf2, text_rect2 = Important.text_objects("Finally you where close to Venus", small_text, textcolor)
        text_rect2.center = (width/2, height/2/2.2)

        text_surf3, text_rect3 = Important.text_objects("Suddenly you smell a scent that you can't place, you look outside", small_text, textcolor)
        text_rect3.center = (width/2, height/2/1.5)

        text_surf4, text_rect4 = Important.text_objects("The bottom of the spaceship has turned red", small_text, textcolor)
        text_rect4.center = (width/2, height/2/1.3)

        text_surf5, text_rect5 = Important.text_objects("The planet is too hot, you have to get away", small_text, textcolor)
        text_rect5.center = (width/2, height/2/1)

        text_surf6, text_rect6 = Important.text_objects("Move left or right with the arrow keys", small_text, textcolor)
        text_rect6.center = (width/2, height/1.6)

        text_surf7, text_rect7 = Important.text_objects("Jump with the up key pause with the p key", small_text, textcolor)
        text_rect7.center = (width/2, height/1.5)

        text_surf8, text_rect8 = Important.text_objects("Reach a score of 650 in 2 minutes to be safe", small_text, textcolor)
        text_rect8.center = (width/2, height/1.4)

        text_surf9, text_rect9 = Important.text_objects("The head (platforms) move down", small_text, textcolor)
        text_rect9.center = (width/2, height/1.3)

        # schrijf naar het scherm
        screen.blit(text_surf1, text_rect1)
        screen.blit(text_surf2, text_rect2)
        screen.blit(text_surf3, text_rect3)
        screen.blit(text_surf4, text_rect4)
        screen.blit(text_surf5, text_rect5)
        screen.blit(text_surf6, text_rect6)
        screen.blit(text_surf7, text_rect7)
        screen.blit(text_surf8, text_rect8)
        screen.blit(text_surf9, text_rect9)

        if Important.button("Start", 150, 500, 100, 50, green, green_button, screen, black, game_loop):
            game_loop()

        if Important.button("Quit", 550, 500, 100, 50, red, red_button, screen, black, quit_game):
            quit_game()
        pg.display.flip()
        clock.tick(30)


def game_loop():
    global point
    global timer
    global paused
    player = pg.Rect(width / 2 - 20, height - 70 - 400, player_width, player_height)
    counter = 0
    point = 0
    coll = []
    timer = pg.font.SysFont("None", 20)
    tempo = 0
    started = False
    game_start_timer = pg.time.get_ticks()
    jump = False
    mixer.init()
    mixer.music.load(path.join(muziek_dir, 'Murdock_-_Stardust_Memories_MDK_remix.MP3'))
    mixer.music.play(-1, 0)

    # game loop
    while True:
        pressed = pg.key.get_pressed()
        if started:
            aux = 1
            tempo = (pg.time.get_ticks() - game_start_timer)//1000
            if aux == tempo:
                aux += 1
                # print(tempo)

        # start the game and timer
        elif pressed[pg.K_UP] or pressed[pg.K_LEFT] or pressed[pg.K_RIGHT]:
            started = True
            game_start_timer = pg.time.get_ticks()

        # event listeners
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game()

        # player move
        pressed = pg.key.get_pressed()
        if pressed[pg.K_LEFT]:
            player = player.move(-10, 0)
        elif pressed[pg.K_RIGHT]:
            player = player.move(10, 0)

        # default platform movement
        player.y += 1
        if point >= 50:
            player.y += 1.5
        if point >= 100:
            player.y += 1.7
        if point >= 250:
            player.y += 1.8
        if point >= 450:
            player.y += 2
        if point >= 650:
            player.y += 2.5
        if point >= 800:
            player.y += 2.8

        # player gravity
        ly = player.y
        player.y += movement_speed

        # pause
        if pressed[pg.K_p]:
            paused = True
            pause()

        # boundaries
        if player.right > width:
            player.x = 0
        if player.left < 0:
            player.x = width - player_width

        # Platforms
        if platforms.__len__() < minimum_platforms:
            # platforms add
            addplatform()
        coll.clear()

        i = 0
        while i < len(platforms):
            platform = platforms[i]
            if platform.__len__() > 0:

                # De snelheid van de platforms berekend met punten
                platform['rect'].top += 1
                if point >= 50:
                    platform['rect'].top += 1.5
                if point >= 100:
                    platform['rect'].top += 1.7
                if point >= 250:
                    platform['rect'].top += 1.8
                if point >= 450:
                    platform['rect'].top += 2
                if point >= 650:
                    platform['rect'].top += 2.5
                if point >= 800:
                    platform['rect'].top += 2.8

            # remove platforms en score
            if platform['rect'].top > height:
                platforms.remove(platform)
                point += 10
                i -= 1
            i += 1

            # game over
            if player.bottom > height:
                game_over()

            # win
            # elif point >= 20 and tempo <= 120:
            elif point >= 650 and tempo <= 120:
                win_game()

            # image platforms
            if platform.__len__() > 0:
                # pg.draw.rect(screen, (0, 225, 0), platform['rect'])
                l = lava
                l = pg.transform.scale(l, (platform['rect'].width, platform['rect'].height))
                screen.blit(l, (platform['rect'].left, platform['rect'].top))

        # platform collision
        onGround = False
        for platform in platforms:
            if platform.__len__() > 0:
                platform_rect = platform['rect']
                py = platform_rect.y - 25

                # check if player moved into y of platform
                if ly + player_height <= py <= player.y + player_height and platform_rect.x - player_width <= player.x + player_width / 2 <= platform_rect.x + platform_rect.width + player_width / 2:
                    player.y = py - player_height
                    onGround = True

        # print("COUNTER: " + str(counter))
        if pressed[pg.K_UP] and not jump and onGround:
            jump = True

        # jump
        if jump:
            counter += 1
            if counter > 8:
                counter = 8
                jump = False

            # jump speed
            player.y -= movement_speed * 6
        elif counter > 0:
            counter -= 1

        if player.bottom > height + 100:
            if not coll.__contains__(True):
                player = player.move(0, movement_speed)

        # draw_world
        screen.blit(rotated_image, player)

        # update screen, fps
        score = timer.render("Score : "+str(point), 0, (225, 225, 225))
        screen.blit(score, (710, 25))
        teller = timer.render("TIME : "+str(tempo), 0, (225, 225, 225))
        screen.blit(teller, (25, 25))
        pg.display.flip()
        screen.blit(background, [-500, 0])
        clock.tick(30)


# intro()
