import pygame
import os
import Important
from random import randint
from os import path

# initialiseren van pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
pygame.mixer.init()
TextFont = pygame.font.SysFont("monospace", 15)

# Setting the screen
size = windowWidth, windowHeight = 800, 600
screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Jupiter Ascending!")

# variable for mainmenu
jupiter_game_completed = False

# colors
white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]
red_button = [150, 0, 0]
green = [0, 255, 0]
green_button = [0, 150, 0]
blue = [0, 0, 255]
grey = [50, 50, 50]
playerColor = [50, 200, 50]
textcolor = [200, 200, 200]

# wolken benodigdheden
wolken = []

# Speler benodigdheden
playerWidth = 35
playerHeight = 35
playerFallSpeed = 3
playerMovementSpeed = 7

# Folder dir
sprites_dir = path.join(path.dirname(__file__), 'sprites')
sound_dir = path.join(path.dirname(__file__), 'sounds')

# Score
Score = 0
blocks_to_pass = 20
Score_cloud = 5
targetscore = blocks_to_pass * Score_cloud * 10
# targetscore = 10    # moet weg
# frames / sec
FPS = pygame.time.Clock()
# for the pause function
pause = False


def crash():
    global Score
    global targetscore
    fail = pygame.mixer.Sound(path.join(sound_dir, "fail2.wav"))
    ####################################
    pygame.mixer.Sound.play(fail)
    pygame.mixer.music.stop()
    ####################################
    largetext = pygame.font.SysFont("algerian", 45)
    textsurf, textrect = Important.text_objects("The spaceship has crashed", largetext, white)
    textrect.center = ((windowWidth/2), (windowHeight/2))
    screen.blit(textsurf, textrect)

    font = pygame.font.SysFont('algerian', 20, bold=True)
    testsurf1, textrect1 = Important.text_objects("You reached a score of " + str(Score) + ' out of ' + str(targetscore), font, white)
    textrect1.center = ((windowWidth/2), (windowHeight/3))
    screen.blit(testsurf1, textrect1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        Important.button("Play Again", 150, 450, 120, 50, green, green_button, screen, black, game_loop)
        Important.button("Quit", 550, 450, 120, 50, red, red_button, screen, black, quitgame)

        pygame.display.update()
        FPS.tick(15)


def score_reached():
    global jupiter_game_completed
    pygame.mixer.music.pause()
    largetext = pygame.font.SysFont("algerian", 30)
    textsurf, textrect = Important.text_objects("Well done, you reached the fuel!", largetext, black)
    textrect.center = ((windowWidth/2), 220)
    text_s, text_r = Important.text_objects("Keep playing or try another planet.", largetext, black)
    text_r.center = ((windowWidth/2), 270)

    screen.blit(textsurf, textrect)
    screen.blit(text_s, text_r)
    jupiter_game_completed = True

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        Important.button("Keep playing", 150, 500, 130, 50, green, green_button, screen, black, unpause)
        Important.button("MainMenu", 550, 500, 130, 50, red, red_button, screen, black, quitgame)

        pygame.display.update()
        FPS.tick(15)


def quitgame():
    pygame.mixer.music.stop()
    import MainMenuV4
    MainMenuV4.main_menu()


def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused():
    pygame.mixer.music.pause()
    large_text = pygame.font.SysFont("algerian", 40)
    text_surf, text_rect = Important.text_objects("Paused", large_text, black)
    text_rect.center = (windowWidth/2, windowHeight/2)
    screen.blit(text_surf, text_rect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        Important.button("Continue", 150, 500, 100, 50, green, green_button, screen, black, unpause)
        Important.button("Restart", 350, 500, 100, 50, green, green_button, screen, black, game_loop)
        Important.button("MainMenu", 550, 500, 100, 50, red, red_button, screen, black, quitgame)

        pygame.display.update()
        FPS.tick(15)


def addwalls():
    num = randint(0, 9)
    if num == 0:  # 1
        nw1 = {'rect': pygame.Rect(100, windowHeight, windowWidth/2, 10), 'color': green}
        nw2 = {'rect': pygame.Rect(300, windowHeight, windowWidth/2, 10), 'color': green}
        made = wolken.append(nw1), wolken.append(nw2)
        return made
    elif num == 1:  # 2
        nw1 = {'rect': pygame.Rect(100, windowHeight, windowWidth/3, 10), 'color': blue}
        nw2 = {'rect': pygame.Rect(450, windowHeight, windowWidth/3, 10), 'color': green}
        made = wolken.append(nw1), wolken.append(nw2)
        return made
    elif num == 2:  # 3
        nw1 = {'rect': pygame.Rect(50, windowHeight, windowWidth/3, 10), 'color': green}
        nw2 = {'rect': pygame.Rect(500, windowHeight, windowWidth/3, 10), 'color': white}
        made = wolken.append(nw1), wolken.append(nw2)
        return made
    elif num == 3:  # 4
        nw1 = {'rect': pygame.Rect(-100, windowHeight, windowWidth / 2, 10), 'color': grey}
        nw2 = {'rect': pygame.Rect(400, windowHeight, windowWidth / 2, 10), 'color': green}
        made = wolken.append(nw1), wolken.append(nw2)
        return made
    elif num == 4:  # 5
        nw1 = {'rect': pygame.Rect(0, windowHeight, windowWidth/2, 10), 'color': green}
        nw2 = {'rect': pygame.Rect(500, windowHeight, windowWidth/2, 10), 'color': grey}
        made = wolken.append(nw1), wolken.append(nw2)
        return made
    elif num == 5:  # 6
        nw1 = {'rect': pygame.Rect(-200, windowHeight, windowWidth/2, 10), 'color': blue}
        nw2 = {'rect': pygame.Rect(300, windowHeight, windowWidth, 10), 'color': grey}
        made = wolken.append(nw1), wolken.append(nw2)
        return made
    elif num == 6:  # 7
        nw1 = {'rect': pygame.Rect(100, windowHeight, windowWidth, 10), 'color': red}
        nw2 = {'rect': pygame.Rect(500, windowHeight, windowHeight, 10), 'color': white}
        made = wolken.append(nw1), wolken.append(nw2)
        return made
    elif num == 7:  # 8
        nw1 = {'rect': pygame.Rect(-600, windowHeight, windowWidth, 10), 'color': white}
        nw2 = {'rect': pygame.Rect(600, windowHeight, windowWidth, 10), 'color': blue}
        made = wolken.append(nw1), wolken.append(nw2)
        return made
    elif num == 8:  # 9
        nw1 = {'rect': pygame.Rect(-100, windowHeight, windowWidth, 10), 'color': red}
        nw2 = {'rect': pygame.Rect(850, windowHeight, windowWidth, 10), 'color': blue}
        made = wolken.append(nw1), wolken.append(nw2)
        return made
    elif num == 9:  # 10
        nw1 = {'rect': pygame.Rect(-650, windowHeight, windowWidth, 10), 'color': blue}
        nw2 = {'rect': pygame.Rect(250, windowHeight, windowWidth, 10), 'color': red}
        made = wolken.append(nw1), wolken.append(nw2)
        return made
    return


def startingwalls():
    global wolken
    w1 = {'rect': pygame.Rect(100, windowHeight, windowWidth/2, 10), 'color': red}
    w2 = {'rect': pygame.Rect(300, windowHeight, windowWidth/2, 10), 'color': blue}

    w3 = {'rect': pygame.Rect(-100, 500, windowWidth/2, 10), 'color': red}
    w4 = {'rect': pygame.Rect(400, 500, windowWidth/2, 10), 'color': blue}

    w5 = {'rect': pygame.Rect(50, 400, windowWidth/3, 10), 'color': red}
    w6 = {'rect': pygame.Rect(500, 400, windowWidth/3, 10), 'color': blue}

    w7 = {'rect': pygame.Rect(100, 300, windowWidth, 10), 'color': red}
    w8 = {'rect': pygame.Rect(500, 300, windowWidth, 10), 'color': blue}

    w9 = {'rect': pygame.Rect(-200, 200, windowWidth/2, 10), 'color': red}
    w10 = {'rect': pygame.Rect(300, 200, windowWidth, 10), 'color': blue}

    w11 = {'rect': pygame.Rect(-650, 100, windowWidth, 10), 'color': red}
    w12 = {'rect': pygame.Rect(250, 100, windowWidth, 10), 'color': blue}

    wolken = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12]


class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(windowWidth / 2 - playerWidth,
                                windowHeight / 2 + playerHeight * 6,
                                playerWidth, playerHeight)

    def move(self, dx, dy):
        # Move each axis separately.
        if dx != 0:
            self.rect.x += dx
            # self.move_single_axis(dx, 0)
        if dy != 0:
            self.rect.y += dy


# ########################################################### P to pause
def game_intro():
    global targetscore
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        screen.fill(black)
        small_text = pygame.font.SysFont("algerian", 20)
        large_text = pygame.font.SysFont("algerian", 35, bold=True)
        text_surf1, text_rect1 = Important.text_objects("Welcome to Jupiter Ascending", large_text, textcolor)
        text_rect1.center = (windowWidth/2, windowHeight/2/3.5)

        text_surf2, text_rect2 = Important.text_objects("The goal is to collect fuel, which can be found at the planet's surface.", small_text, textcolor)
        text_rect2.center = (windowWidth/2, windowHeight/2/2)

        text_surf3, text_rect3 = Important.text_objects("However there is only one path.", small_text, textcolor)
        text_rect3.center = (windowWidth/2, windowHeight/2/1.5)

        text_surf4, text_rect4 = Important.text_objects("Don't get held back by the clouds,", small_text, textcolor)
        text_rect4.center = (windowWidth/2, windowHeight/2/1.2)

        text_surf5, text_rect5 = Important.text_objects("Or you will lose the only path there is.", small_text, textcolor)
        text_rect5.center = (windowWidth/2, windowHeight/2)

        text_surf6, text_rect6 = Important.text_objects("Move left with the left arrow key or with the 'A' key.", small_text, textcolor)
        text_rect6.center = (windowWidth/2, windowHeight/1.7)

        text_surf7, text_rect7 = Important.text_objects("Move right with the right arrow key or with the 'D' key.", small_text, textcolor)
        text_rect7.center = (windowWidth/2, windowHeight/1.6)

        text_surf9, text_rect9 = Important.text_objects("Press 'P' to pause.", small_text, textcolor)
        text_rect9.center = (windowWidth/2, windowHeight/1.5)

        text_surf8, text_rect8 = Important.text_objects("Reach a score of " + str(targetscore) + " to win. Good luck!", small_text, textcolor)
        text_rect8.center = (windowWidth/2, windowHeight/1.3)

        # schrijf naar het scherm
        screen.blit(text_surf1, text_rect1), screen.blit(text_surf2, text_rect2), screen.blit(text_surf3, text_rect3)
        screen.blit(text_surf4, text_rect4), screen.blit(text_surf5, text_rect5), screen.blit(text_surf6, text_rect6)
        screen.blit(text_surf7, text_rect7), screen.blit(text_surf8, text_rect8), screen.blit(text_surf9, text_rect9)

        Important.button("Start", 150, 500, 100, 50, green, green_button, screen, black, game_loop)
        Important.button("Quit", 550, 500, 100, 50, red, red_button, screen, black, quitgame)
        pygame.display.update()
        FPS.tick(15)


def game_loop():
    global Score
    global pause
    global blocks_to_pass
    global Score_cloud
    Score = 0

    # speler maken
    player = Player()

    # beginmuren positioneren
    startingwalls()

    # music
    mainmusic = path.join(sound_dir, 'mainmusic.mp3')
    secondarymusic = path.join(sound_dir, 'secondarymusic.mp3')
    r = randint(0, 1)
    if r == 0:
        music = mainmusic
    else:
        music = secondarymusic

    # sound
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)

    # images
    cloudimage = pygame.image.load(path.join(sprites_dir, 'clouds.png'))
    jupiter = pygame.image.load(path.join(sprites_dir, 'jupiter_far1.png'))
    jupiter = pygame.transform.scale(jupiter, (800, 800))
    bg = jupiter.get_rect()
    bg = bg.move((0, -100))
    player_ship_down = pygame.image.load(path.join(sprites_dir, 'Playership64_down.gif'))
    player_ship_down = pygame.transform.scale(player_ship_down, (35, 35))
    player_ship_left = pygame.image.load(path.join(sprites_dir, 'Playership64_left.gif'))
    player_ship_left = pygame.transform.scale(player_ship_left, (35, 35))
    player_ship_right = pygame.image.load(path.join(sprites_dir, 'Playership64_right.gif'))
    player_ship_right = pygame.transform.scale(player_ship_right, (35, 35))
    player_ship = player_ship_down

    # muren
    move_up_speed = -1
    minimum_clouds = 12
    blocks_passed = 0

    # speler collision
    pcb, pcl, pcr, pct = [], [], [], []

    continue_game = True
    ship_rotation = ""

    # The actual game
    while True:
        # frames / sec
        FPS.tick(60)
        # scherm zwart maken
        screen.fill(black)
        # afbeelding op het scherm zetten
        screen.blit(jupiter, bg)

        # check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        # Move the player if a button is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            if not ship_rotation == "links":
                # afbeelding naar links draaien
                ship_rotation = "links"
                player_ship = player_ship_left
            if not player.rect.left < 0:
                player.move(-playerMovementSpeed, 0)
        elif key[pygame.K_RIGHT] or key[pygame.K_d]:
            if not ship_rotation == "rechts":
                # afbeelding naar rechts draaien
                ship_rotation = "rechts"
                player_ship = player_ship_right

            if not player.rect.right > windowWidth:
                player.move(playerMovementSpeed, 0)
        else:
            # afbeelding weer rechtop zetten
            if ship_rotation == "rechts":
                ship_rotation = ""
                # draai 90 graden naar links
                player_ship = player_ship_down
            elif ship_rotation == "links":
                ship_rotation = ""
                # draai 90 graden naar rechts
                player_ship = player_ship_down

        if key[pygame.K_p]:
            pause = True
            paused()
        # als wolken minder bevat dan het minimumaanatal wolken
        if wolken.__len__() < minimum_clouds:
            addwalls()

        # clear collision lists
        pcb.clear(), pcl.clear(), pcr.clear(), pct.clear()

        # Perform for every wolk in wolken
        for wolk in wolken[:]:
            # if wolk contains something
            if wolk.__len__() > 0:
                # move wolk up
                wolk['rect'].top += move_up_speed
                # check if the player has collided with a cloud
                if player.rect.colliderect(wolk['rect']):
                    player.move(0, move_up_speed)

                    # als de bovenkant van de wolk lager is dan de onderkant van de speler
                    if wolk['rect'].top <= player.rect.bottom:
                        pcb.append(True)
                    # als de bovenkant van de speler tussen de hoogte van de wolk in is
                    if wolk['rect'].top <= player.rect.top <= wolk['rect'].bottom:
                        pct.append(True)
                    # als de rechterkant van de wolk tussen de linkerkant van de speler in is
                    elif player.rect.topleft[1] <= wolk['rect'].midright[1] <= player.rect.bottomleft[1]:
                        pcl.append(True)
                    # als de linkerkant van de wolk tussen de rechterkant van de speler in is
                    elif player.rect.topright[1] <= wolk['rect'].midleft[1] <= player.rect.bottomright[1]:
                        pcr.append(True)

                if wolk['rect'].bottom < 0:
                    wolken.remove(wolk)
                    Score += Score_cloud
                    blocks_passed += 1

            if wolk.__len__() > 0:
                # afbeelding op de plaats van de wolk tekenen
                cl = cloudimage
                cl = pygame.transform.scale(cl, (wolk['rect'].width, wolk['rect'].height))
                screen.blit(cl, (wolk['rect'].left, wolk['rect'].top))

        # als er x aantal blokjes voorbij zijn dan de snelheid verhogen
        if blocks_passed == blocks_to_pass:
            move_up_speed = move_up_speed - 0.15
            blocks_passed = 0

        # als de speler niet lager is dan de onderkant van het scherm
        if not player.rect.bottom > windowHeight:
            # als de lijst geen "True" bevat
            if not pcb.__contains__(True):
                # Move player down
                player.move(0, playerFallSpeed)

            if not player.rect.left < 0 or player.rect.right > windowWidth:
                if pct.__contains__(True):
                    # stop player from having its head stuck in the block
                    player.move(0, playerFallSpeed)
                if pcr.__contains__(True):
                    # stop player from moving right
                    player.move(-playerMovementSpeed, playerFallSpeed)
                if pcl.__contains__(True):
                    # stop player from moving left
                    player.move(playerMovementSpeed, playerFallSpeed)

        # als de bovenkant van de speler boven het scherm is
        if player.rect.top < 0:
            crash()

        # als de score behaald is
        if Score >= targetscore:
            if continue_game:
                continue_game = False
                pause = True
                score_reached()

        # score op scherm schrijven
        Important.texts(TextFont, Score, white, screen)

        # draw player to screen
        screen.blit(player_ship, player.rect)

        # draw to screen
        pygame.display.flip()


# uncomment when testing
# game_intro()
