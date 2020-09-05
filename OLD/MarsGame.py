

#     dinsdag 1700 16-1-2018
# variable for mainmenu
mars_game_completed = False
# project 2 maandag ochtend 1400
def myGame():
    import turtle
    import math
    import time
    import pygame

    image = "Mars_Folder/img/mars.gif"

    wn = turtle.Screen()

    wn.title("Mars spel")
    wn.setup(800, 600)
    wn.bgpic(image)
    introDone = False

    def game1():

        pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
        pygame.init()
        # song = pygame.mixer.Sound('music/music.wav')
        pygame.mixer.music.load('Mars_Folder/music/music.wav')
        pygame.mixer.music.play(-1)

        global playerGold
        class Pen(turtle.Turtle):
            def __init__(self):
                turtle.Turtle.__init__(self)
                self.shape("square")
                self.color("white")
                self.penup()
                self.speed(0)

        class Player(turtle.Turtle):
            def __init__(self):
                turtle.Turtle.__init__(self)
                self.shape("square")
                self.color("blue")
                self.penup()
                self.speed(0)
                self.gold = 100


            def go_up(self):
                move_to_x = player.xcor()
                move_to_y = player.ycor() + 24
                if (move_to_x, move_to_y) not in walls:
                    self.goto(move_to_x, move_to_y)

            def go_down(self):
                move_to_x = player.xcor()
                move_to_y = player.ycor() - 24
                if (move_to_x, move_to_y) not in walls:
                    self.goto(move_to_x, move_to_y)


            def go_left(self):
                move_to_x = player.xcor() - 24
                move_to_y = player.ycor()
                if (move_to_x, move_to_y) not in walls:
                    self.goto(move_to_x, move_to_y)

            def go_right(self):
                move_to_x = player.xcor() + 24
                move_to_y = player.ycor()
                if (move_to_x, move_to_y) not in walls:
                    self.goto(move_to_x, move_to_y)

            def is_collision(self, other):
                a = self.xcor()-other.xcor()
                b = self.ycor()-other.ycor()
                distance = math.sqrt((a ** 2) + (b ** 2) )

                if distance < 5:
                    return True
                else:
                    return False

        class treasure(turtle.Turtle):
            def __init__(self, x, y):
                turtle.Turtle.__init__(self)
                self.shape("circle")
                self.color("gold")
                self.penup()
                self.speed(0)
                self.gold = 100
                self.goto(x, y)

            def destroy(self):
                self.goto(2000, 2000)
                self.hideturtle()

        levels = [""]

        level_1 = [
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXP   XXXXXXXXXXXXXXXXXXX",
            "XX XX  XXXXXXXXXXXXXXXXXX",
            "XX XXX   XXXXXXXXXXXXXXXX",
            "XX XXXX  XXXXXXXXXXXXXXXX",
            "XX XXXXX   XXXXXXXXXXXXXX",
            "XX XXXXXXX   XXXXXXXXXXXX",
            "XX XXXXXXXXX   XXXXXXXXXX",
            "XX XXXXXXXXXXX   XXXXXXXX",
            "XX XXXXXXXXXXX  XXXXXXXXX",
            "XX  XXX     XX  XXXXXXXXX",
            "X       XXX             X",
            "XXXXXXXXXXXXXXXXX  XXXXXX",
            "XXXXXXXXXXXXXXX    XXXXXX",
            "XXXXXXXXXXXXXX   XXXXXXXX",
            "XXXXXXXXXXXXX  XXXXXXXXXX",
            "XXXXXXXXXXXXXX  XXXXXXXXX",
            "XXXXXXXXXXXXXXX  XXXXXXXX",
            "XXXXXXXXXXXXXXXX  XXXXXXX",
            "XXXXXXXXXXXXXXXXX  XXXXXX",
            "XXXXXXXXXXXXXXXXXX  XXXXX",
            "XXXXXXXXXXXXXXXXXXX  XXXX",
            "XXXXXXXXXXXXXXXXXXXX  TXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXX"
        ]

        treasuress = []


        levels.append(level_1)

        def setup_maze(level):
            for y in range(len(level)):
                for x in range(len(level[y])):
                    character = level[y][x]

                    screen_x = -288 + (x * 24)
                    screen_y = 288 - (y * 24)

                    if character == "X":
                        pen.goto(screen_x, screen_y)
                        pen.stamp()
                        walls.append((screen_x, screen_y))

                    if character == "P":
                        player.goto(screen_x, screen_y)

                    if character == "T":
                        treasuress.append(treasure(screen_x, screen_y))

        pen = Pen()
        player = Player()

        walls = []


        setup_maze(levels[1])

        turtle.listen()
        turtle.onkey(player.go_left, "Left")
        turtle.onkey(player.go_right, "Right")
        turtle.onkey(player.go_up, "Up")
        turtle.onkey(player.go_down, "Down")

        wn.tracer(0)

        while True:
            for treasure in treasuress:
                if player.is_collision(treasure):
                    turtle.clearscreen()
                    game2()
            wn.update()

    def game2():
        global playerGold
        class Pen(turtle.Turtle):
            def __init__(self):
                turtle.Turtle.__init__(self)
                self.shape("square")
                self.color("white")
                self.penup()
                self.speed(0)

        class Player(turtle.Turtle):
            def __init__(self):
                turtle.Turtle.__init__(self)
                self.shape("square")
                self.color("blue")
                self.penup()
                self.speed(0)
                self.gold = 100


            def go_up(self):
                move_to_x = player.xcor()
                move_to_y = player.ycor() + 24
                if (move_to_x, move_to_y) not in walls:
                    self.goto(move_to_x, move_to_y)

            def go_down(self):
                move_to_x = player.xcor()
                move_to_y = player.ycor() - 24
                if (move_to_x, move_to_y) not in walls:
                    self.goto(move_to_x, move_to_y)


            def go_left(self):
                move_to_x = player.xcor() - 24
                move_to_y = player.ycor()
                if (move_to_x, move_to_y) not in walls:
                    self.goto(move_to_x, move_to_y)

            def go_right(self):
                move_to_x = player.xcor() + 24
                move_to_y = player.ycor()
                if (move_to_x, move_to_y) not in walls:
                    self.goto(move_to_x, move_to_y)

            def is_collision(self, other):
                a = self.xcor()-other.xcor()
                b = self.ycor()-other.ycor()
                distance = math.sqrt((a ** 2) + (b ** 2) )

                if distance < 5:
                    return True
                else:
                    return False

        class treasure(turtle.Turtle):
            def __init__(self, x, y):
                turtle.Turtle.__init__(self)
                self.shape("circle")
                self.color("gold")
                self.penup()
                self.speed(0)
                self.gold = 100
                self.goto(x, y)

            def destroy(self):
                self.goto(2000, 2000)
                self.hideturtle()

        levels = [""]

        level_1 = [
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXX              XXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "X                       X",
            "X                       X",
            "X                 P    TX",
            "X                       X",
            "X                       X",
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXX XXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXX XXXXX"
        ]

        treasuress = []


        levels.append(level_1)

        def setup_maze(level):
            turtle.bgcolor("black")
            for y in range(len(level)):
                for x in range(len(level[y])):
                    character = level[y][x]

                    screen_x = -288 + (x * 24)
                    screen_y = 288 - (y * 24)

                    if character == "X":
                        pen.goto(screen_x, screen_y)
                        pen.stamp()
                        walls.append((screen_x, screen_y))

                    if character == "P":
                        player.goto(screen_x, screen_y)

                    if character == "T":
                        treasuress.append(treasure(screen_x, screen_y))

        pen = Pen()
        player = Player()

        walls = []


        setup_maze(levels[1])

        turtle.listen()
        turtle.onkey(player.go_left, "Left")
        turtle.onkey(player.go_right, "Right")
        turtle.onkey(player.go_up, "Up")
        turtle.onkey(player.go_down, "Down")

        wn.tracer(0)

        while True:
            for treasure in treasuress:
                if player.is_collision(treasure):
                    outro()
            wn.update()

    def intro():
        pen1 = turtle.Pen()

        pen1.color('black')

        turtle.clearscreen()

        pen1.up()
        pen1.goto(0, 100)
        pen1.down()
        pen1.write("ello! *instructions* ", False, 'center', font=('Arial', 24, 'bold'))
        time.sleep(5)
        turtle.clearscreen()
        wn.bgpic(image)
        introDone = True

    def outro():
        global mars_game_completed
        mars_game_completed = True
        import MainMenuV4
        MainMenuV4.main_menu()
        pygame.display.iconify()

        import time
        from turtle import Pen
        pen1 = Pen()

        pen1.color('black', 'green')

        turtle.clearscreen()

        pen1.up()
        pen1.goto(0, 100)
        pen1.down()
        pen1.write("You win!", False, 'center', font=('Cooper Black', 18, 'bold'))
        time.sleep(2)
        turtle.clearscreen()
        turtle.done()


    # def backgroundImage():
    #
    #
    #     def test():
    #         from turtle import *
    #         from Tkinter import *
    #         wn.bgpic('warehouse1.gif')
    #         fd(100)
    #         goto(50, 100)
    #         mainloop()
    #
    #     test()

    if introDone == False:
        intro()
    game1()

# play the game:
# myGame()
