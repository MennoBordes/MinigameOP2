# -*- coding: utf-8 -*-
import sys, random
import pygame
from os import path
uranus_game_completed = False


def menno():
    pygame.init()
    pygame.mixer.init()
    WIDTH = 800
    HEIGHT = 600
    gameScreen = pygame.display.set_mode([WIDTH, HEIGHT])
    # pygame.display.set_caption('MemoryGame')

    resources_dir = path.join(path.dirname(__file__), 'resources')
    card_back = pygame.image.load(path.join(resources_dir, 'uranus.png')).convert_alpha()
    card_fox = pygame.image.load(path.join(resources_dir, 'Aquarius.png')).convert_alpha()
    card_dachshund = pygame.image.load(path.join(resources_dir, 'Aries.png')).convert_alpha()
    card_moose = pygame.image.load(path.join(resources_dir, 'Cancer.png')).convert_alpha()
    card_bear = pygame.image.load(path.join(resources_dir, 'Capricorn.png')).convert_alpha()
    card_beaver = pygame.image.load(path.join(resources_dir, 'Gemini.png')).convert_alpha()
    card_cat = pygame.image.load(path.join(resources_dir, 'Leo.png')).convert_alpha()
    card_duck = pygame.image.load(path.join(resources_dir, 'Libra.png')).convert_alpha()
    card_elephant = pygame.image.load(path.join(resources_dir, 'Pisces.png')).convert_alpha()
    card_horse = pygame.image.load(path.join(resources_dir, 'Sagittarius.png')).convert_alpha()
    card_leopard = pygame.image.load(path.join(resources_dir, 'Scorpio.png')).convert_alpha()
    card_rabbit = pygame.image.load(path.join(resources_dir, 'Taurus.png')).convert_alpha()
    card_squirrel = pygame.image.load(path.join(resources_dir, 'Virgo.png')).convert_alpha()
    menu_image = pygame.image.load(path.join(resources_dir, 'gameMenu.png')).convert()
    end_image = pygame.image.load(path.join(resources_dir, 'gameEnd.png')).convert()
    memory_text = pygame.image.load(path.join(resources_dir, 'memorytext.png')).convert_alpha()

    cardSize = card_back.get_rect().size

    allCardsList = [card_fox, card_dachshund, card_bear, card_moose,
                    card_beaver, card_cat, card_duck, card_elephant,
                    card_horse, card_leopard, card_rabbit, card_squirrel
                    ]

    def Text(screen, text, size, color, coords):
        lfont = pygame.font.SysFont('algerian', size)
        labl = lfont.render(text, 1, color)
        screen.blit(labl, coords)

    class Card:
        def __init__(self, x, y, picture):
            global clickable, pause
            self.x = x
            self.y = y
            self.pic = picture
            self.card = card_back
            self.commenceaction = False
            clickable = True
            pause = False

        def mouse(self, pos, click):
            global last
            if not pause:
                if clickable:
                    if self.x + cardSize[0] > pos[0] > self.x and self.y + cardSize[1] > pos[1] > self.y:
                        if click[0]:
                            last = pygame.time.get_ticks()
                            self.card = self.pic
                            if self in mouseClicks:
                                pass
                            elif self in openedCards:
                                pass
                            else:
                                mouseClicks.append(self)

        def flipBack(self):
            self.card = card_back

        def drawCard(self, scren):
            scren.blit(self.card, [self.x, self.y])

    class Button:
        def __init__(self, xpos, ypos, height, width, buttontext, regularcolor, hovercolor, clickcolor, function, size=30, textfont='Arial Bold'):
            global clickableButton
            self.function = function
            self.buttontext = buttontext
            self.currentcolor = regularcolor
            self.clickcolor = clickcolor
            self.hovercolor = hovercolor
            self.regularcolor = regularcolor
            self.width = width
            self.height = height
            self.ypos = ypos
            self.xpos = xpos
            self.commenceaction = False
            self.font = pygame.font.SysFont(textfont, size)
            self.textcontent = self.font.render(self.buttontext, 1, (10, 10, 10))
            self.textposition = pygame.Rect((self.xpos, self.ypos), (self.width, self.height))
            self.textposition[0] = self.xpos + ((self.width - self.textcontent.get_width()) / 2)
            self.textposition[1] = self.ypos + ((self.width - self.textcontent.get_height()) / 6)
            clickableButton = True

        def mousemovement(self, position, key):
            if clickableButton:
                if self.xpos < position[0] < self.xpos + self.width and self.ypos < position[1] < self.ypos + self.height:
                    if key[0]:
                        self.currentcolor = self.clickcolor
                        self.commenceaction = True
                    else:
                        self.currentcolor = self.hovercolor
                        if self.commenceaction:
                            self.function()
                            self.commenceaction = False
                else:
                    self.currentcolor = self.regularcolor

        def drawbutton(self, scren):
            pygame.draw.rect(scren, self.currentcolor, pygame.Rect((self.xpos, self.ypos), (self.width, self.height)))
            scren.blit(self.textcontent, self.textposition)

    class Cards:
        def __init__(self):
            self.cards = []

        def board(self, grid):
            for card in allCardsList:
                for i in range(2):
                    position = random.randint(0, len(grid)-1)
                    self.cards.append(Card(grid[position][0], grid[position][1], card))
                    grid.pop(position)

        def click(self):
            for cardclick in self.cards:
                cardclick.opened()

        def mouse(self, pos, click):
            for cardmouse in self.cards:
                cardmouse.mouse(pos, click)

        def drawBoard(self, display):
            for draw in self.cards:
                draw.drawCard(display)

        def clearList(self):
            del self.cards[:]

    class Allbuttons:
        def __init__(self, allthebuttons):
            self.buttons = allthebuttons

        def drawbutton(self, scren):
            for button in self.buttons:
                button.drawbutton(scren)

        def mousemovement(self, position, key):
            for button in self.buttons:
                button.mousemovement(position, key)

    class Status():
        menu = 1
        game = 2
        fade = 3
        end = 4
        info = 5

    class Game:
        def __init__(self, screen):
            global mouseClicks, openedCards
            self.currentStatus = Status.menu
            self.currentScreen = screen
            self.screenRect = self.currentScreen.get_rect()
            self.cards = Cards()
            self.correct = None
            self.clickNow = 0
            self.t1 = 0
            self.playtime = 0
            self.clickedTime = 0
            self.addTime = False
            self.timerPause = False
            self.clock = pygame.time.Clock()
            self.clock2 = pygame.time.Clock()
            self.clock3 = pygame.time.Clock()
            self.surface = pygame.Surface((WIDTH, HEIGHT))
            self.surface.fill((0, 200, 0))
            self.surfaceAlpha = 0

            openedCards = []
            mouseClicks = []

        def makeGrid(self):
            gridList = []

            for i in range(4):  # cards in vertical |
                y = 55 + (i*1)
                y += i*cardSize[1]
                for j in range(6):  # cards in horizontal --
                    x = 15 + (j*1)
                    x += j*cardSize[0]
                    f = x, y
                    gridList.append(f)

            random.shuffle(gridList)

            return gridList

        def turnCards(self):
            global clickable, last
            if len(mouseClicks) == 2:
                pygame.display.flip()
                if mouseClicks[0].pic is mouseClicks[1].pic:
                    self.correct = True
                    openedCards.append(mouseClicks[0]); openedCards.append(mouseClicks[1])
                    del mouseClicks[:]
                else:
                    clickable = False
                    self.correct = False
                    self.clickNow = pygame.time.get_ticks()
                    if self.clickNow - last >= 1200:
                        self.correct = None
                        last = self.clickNow
                        clickable = True
                        mouseClicks[0].flipBack(); mouseClicks[1].flipBack()
                        del mouseClicks[:]

        def correctWrong(self):
            if self.correct:
                self.clickNow = pygame.time.get_ticks()
                Text(self.currentScreen, 'CORRECT', 30, (0, 220, 0), (self.screenRect.centerx-0, 20))
                if self.clickNow - last >= 1200:
                    self.correct = None
            elif self.correct == False:
                Text(self.currentScreen, 'WRONG', 30, (255, 0, 0), (self.screenRect.centerx-0, 20))

        def ifOpened(self):
            if len(openedCards) == len(allCardsList)*2:
                self.currentStatus = Status.end
                self.gameEnd()
            # self.gameEnd()    # om eindscherm te testen

        def timer(self):
            if not self.timerPause:
                if pause:
                    self.t1 = self.clock2.tick()
                else:
                    milliseconds = (self.now - self.t1)
                    seconds = milliseconds / 1000
                    self.playtime += seconds
                    self.t1 = 0

        def writeFile(self, score):
            file = open('scores.txt', 'w')
            file.write(str(score))
            file.close()

        def readFile(self):
            file = open('scores.txt', 'r')
            score = file.readline()
            file.close()
            return score

        def showMenu(self):
            global buttons
            self.currentStatus = Status.info
            self.cards.clearList()
            self.playtime = 0
            self.correct = None
            self.addTime = False
            self.timerPause = False
            self.surfaceAlpha = 0
            del openedCards[:]
            del mouseClicks[:]
            buttons = Allbuttons([
                Button(self.screenRect.centerx-50, self.screenRect.centery-30, 40, 100, 'PLAY', (0, 4, 255), (10,240,110), (160,245,225), self.startGame),
                Button(self.screenRect.centerx-50, self.screenRect.centery+20, 40, 100, 'EXIT', (0, 4, 255), (10,240,110), (160,245,225), self.quitGame)
                ])

        def startGame(self):
            global buttons
            self.currentStatus = Status.game
            self.cards.board(self.makeGrid())
            buttons = Allbuttons([
                Button(810, 25, 30, 70, 'EXIT', (0, 4, 255), (10,240,110), (160,245,225), self.quitGame, 26),
                Button(640, 25, 30, 70, 'BACK', (0, 4, 255), (10,240,110), (160,245,225), self.showMenu, 26)
                ])

        def infoTab(self):
            global buttons
            self.currentStatus = Status.info
            buttons = Allbuttons([
                Button(self.screenRect.centerx-50, 600, 40, 100, 'BACK', (0, 4, 255), (10,240,110), (160,245,225), self.showMenu,),
            ])

        def goPause(self):
            global pause
            if pause:
                pygame.mixer.music.unpause()
                pause = False
            else:
                pygame.mixer.music.pause()
                pause = True

        def goFade(self):
            global clickableButton
            self.surfaceAlpha = min(255, self.surfaceAlpha + (self.now/1000) * 210)
            self.surface.set_alpha(self.surfaceAlpha)
            self.currentScreen.blit(self.surface, (0, 0))
            self.timerPause = True
            clickableButton = False
            if self.surfaceAlpha == 255:
                self.gameEnd()
            sound = pygame.mixer.Sound(sound_win)
            sound.set_volume(.4)
            sound.play()

        def gameEnd(self):
            global buttons, clickableButton
            self.currentStatus = Status.end
            global uranus_game_completed
            uranus_game_completed = True
            clickableButton = True
            buttons = Allbuttons([
                Button(self.screenRect.centerx-135, 500, 40, 90, 'MENU', (0,200,0), (10,240,110), (160,245,225), self.showMenu),
                Button(self.screenRect.centerx+45, 500, 40, 90, 'EXIT', (0,200,0), (10,240,110), (160,245,225), self.quitGame)
            ])
            pygame.mixer.music.stop()
            # self.currentSound = music_menu
            # pygame.mixer.music.load(music_menu)
            # pygame.mixer.music.play(-1)

        def quitGame(self):
            pygame.mixer.music.stop()
            import MainMenuV4
            MainMenuV4.main_menu()

        def updateScreen(self):
            global buttons
            self.now = self.clock.tick()

            if self.currentStatus == Status.menu:
                self.currentScreen.blit(menu_image, (0, 0))
                buttons.drawbutton(self.currentScreen)

                pygame.display.flip()

            elif self.currentStatus == Status.info:
                self.currentScreen.blit(menu_image, (0, 0))
                buttons.drawbutton(self.currentScreen)
                self.currentScreen.blit(memory_text, (self.screenRect.centerx-120, 20))
                Text(self.currentScreen, 'INFO', 40, (255, 255, 255), (self.screenRect.centerx-20, 75))
                Text(self.currentScreen, 'Click on the images', 40, (255, 255, 255), (270, 110))
                Text(self.currentScreen, 'Open 2 images that are the same', 30, (255, 255, 255), (220, 150))
                Text(self.currentScreen, 'You win if you open all the images', 30, (255, 255, 255), (200, 180))

                pygame.display.flip()

            elif self.currentStatus == Status.game or self.currentStatus == Status.fade:
                buttons.drawbutton(self.currentScreen)
                self.currentScreen.blit(memory_text, (10, 20))
                pygame.draw.line(self.currentScreen, [0, 0, 0], [0, 70], [WIDTH, 70])
                self.cards.drawBoard(self.currentScreen)
                self.timer()
                Text(self.currentScreen, str(round(self.playtime, 1)), 30, (225, 0, 0), (self.screenRect.centerx-80, 20))
                if pause:
                    Text(self.currentScreen, 'GAME PAUSED', 70, (225, 0, 0), (self.screenRect.centerx-180, self.screenRect.centery))
                self.correctWrong()
                self.turnCards()
                self.ifOpened()
                if self.currentStatus == Status.fade:
                    self.goFade()
                pygame.display.flip()
                self.currentScreen.fill([0, 0, 153])

            elif self.currentStatus == Status.end:
                self.currentScreen.blit(end_image, (0, 0))
                buttons.drawbutton(self.currentScreen)
                pygame.display.flip()

    game = Game(gameScreen)
    game.showMenu()

    def menno2():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # print("menno2 fout")
                    pygame.mixer.music.stop()
                    import MainMenuV4
                    MainMenuV4.main_menu()

                if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    buttons.mousemovement(pygame.mouse.get_pos(), pygame.mouse.get_pressed())

                if event.type == pygame.MOUSEBUTTONDOWN:
                    game.cards.mouse(pygame.mouse.get_pos(), pygame.mouse.get_pressed())

            game.updateScreen()
    menno2()
# menno()



