mars_game_completed = False


def hisGame():
    import pygame


    #     dinsdag 1700 16-1-2018

    # project 2 maandag ochtend 1400

    def myGame():

        import turtle
        import math
        import time
        import pygame
        import random
        from os import path

        img_dir = path.join(path.dirname(__file__), 'img')
        music_dir = path.join(path.dirname(__file__), 'music')
        image = path.join(img_dir, 'mars.gif')

        wn = turtle.Screen()

        wn.title("Mars spel")
        wn.setup(800, 600)

        wn.bgpic(image)
        introDone = False

        def game1():
            wn.bgpic(image)
            wn.tracer(0)
            pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
            pygame.init()
            # song = pygame.mixer.Sound('music/music.wav')
            pygame.mixer.music.load(path.join(music_dir, 'music.wav'))
            pygame.mixer.music.play(-1)

            turtle.register_shape(path.join(img_dir, 'playerShip64.GIF'))

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
                    self.shape(path.join(img_dir, 'playerShip64.GIF'))
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

            class Enemy(turtle.Turtle):
                turtle.register_shape(path.join(img_dir, 'mete.gif'))
                def __init__(self, x, y):
                    turtle.Turtle.__init__(self)
                    self.color("yellow")
                    self.penup()
                    self.speed(-50)
                    self.gold = 100
                    self.goto(x, y)
                    self.direction = random.choice(["up", "down", "left", "right"])

                def move(self):
                    if self.direction == "up":
                        dx = 0
                        dy = 24
                    elif self.direction == "down":
                        dx = 0
                        dy = -24
                    elif self.direction == "left":
                        dx = -24
                        dy = 0
                    elif self.direction == "right":
                        dx = 24
                        dy = 0
                    else:
                        dx = 0
                        dy = 0

                    move_to_x = self.xcor() + dx
                    move_to_y = self.ycor() + dy

                    if (move_to_x, move_to_y) not in walls:
                        self.goto(move_to_x, move_to_y)
                    else:
                        self.direction = random.choice(["up", "down", "left", "right"])

                    turtle.ontimer(self.move, t=random.randint(100, 300))

                def destroy(self):
                    self.goto(2000,2000)
                    self.hideturtle()


            levels = [""]

            level_1 = [
                "XXXXXXXXXXXXXXXXXXXXXXXXX",
                "XXP   T  XXXXXXXXXXXXXXXX",
                "XX XX    XXXXXXX    E  XX",
                "XX XXX   XXXXXXX  XXX  XX",
                "XX  XXX  XXXXXXX  XXX  XX",
                "XX  XXX           XXX  XX",
                "XXX  XX   E       XXX  XX",
                "XXX  XXXXXXX   XXXXXX  XX",
                "XX   XXXXXXXXX   XX    XX",
                "XXXXXXXXXXXXXX  XXX    XX",
                "XX  XXX     XX  XXXXXXXXX",
                "X       XXX             X",
                "XXXXXXXXXXXXXXXXX  XXXXXX",
                "XXXXXXXXXXXXXXX    XXXXXX",
                "XXXXX  XXXXXXX   XXXXXXXX",
                "XXXXX  XXXXXX  XXXXXXXXXX",
                "XXXXXXXXXXXXXX  XXXXXXXXX",
                "XXXXXXXXXXXXXXX  XXXXXXXX",
                "XXXXXXXXXXXXXXX   XXXXXXX",
                "XXXX               XXXXXX",
                "XXXX         E      XXXXX",
                "XXXXXXXXXXXXXXXXXXX  XXXX",
                "XXXXXXXXXXXXXXXXXXXX  TXX",
                "XXXXXXXXXXXXXXXXXXXXXXXXX"
            ]

            level_2 = [
                "XXXXXXXXXXXXXXXXXXXXXXXXX",
                "XXP   T  XXXXXXXXXXXXXXXX",
                "XX XX    XXXXXXX    E  XX",
                "XX XXX   XXXXXXX  XXX  XX",
                "XX  XXX  XXXXXXX  XXX  XX",
                "XX  XXX           XXX  XX",
                "XXX  XX   E       XXX  XX",
                "XXX  XXXXXXX   XXXXXX  XX",
                "XX   XXXXXXXXX   XX    XX",
                "XXXXXXXXXXXXXX  XXX    XX",
                "XX  XXX     XX  XXXXXXXXX",
                "X       XXX             X",
                "XXXXXXX            XXXXXX",
                "XXXXXXX            XXXXXX",
                "XXXXX            XXXXXXXX",
                "XXXXX          XXXXXXXXXX",
                "XXXXXXXXXXXXXX  XXXXXXXXX",
                "XXXXXXXXXXXXXXX  XXXXXXXX",
                "XXXXXXXXXXXXXXX   XXXXXXX",
                "XXXX               XXXXXX",
                "XXXX         E      XXXXX",
                "XXXXXXXXXXXXXXXXXXX  XXXX",
                "XXXXXXXXXXXXXXXXXXXX  TXX",
                "XXXXXXXXXXXXXXXXXXXXXXXXX"
            ]

            level_3 = [
                "XXXXXXXXXXXXXXXXXXXXXXXXX",
                "XXP  T   XXXXXXXXXXXXXXXX",
                "XX XX    XXXXXXX    E  XX",
                "XX XXX   XXXXXXX  XXX  XX",
                "XX  XXX  XXXXXXX  XXX  XX",
                "XX  XXX           XXX  XX",
                "XXX  XX   E       XXX  XX",
                "XXX  XXXXXXX   XXXXXX  XX",
                "XX   XXXXXXXXX   XX    XX",
                "XXXXXXXXXXXXXX  XXX    XX",
                "XX  XXX     XX  XXXXXXXXX",
                "X       XXX             X",
                "XXXXXXXXXXXXXXXXX  XXXXXX",
                "XXXXXXXXXXXXXXX    XXXXXX",
                "XXXXX  XXXXXXX   XXXXXXXX",
                "XXXXX  XXXXXX  XXXXXXXXXX",
                "XXXXXXXXXXXXXX  XXXXXXXXX",
                "XXXXXXXXXXXXXXX  XXXXXXXX",
                "XXXXXXXXXXXXXXX   XXXXXXX",
                "XXXX               XXXXXX",
                "XXXX         E      XXXXX",
                "XXXXXX               XXXX",
                "XXXXX                 TXX",
                "XXXXXXXXXXXXXXXXXXXXXXXXX"
            ]

            level_4 = [
                "XXXXXXXXXXXXXXXXXXXXXXXXX",
                "XXPX  XEEEE   XXXXXXXXXXX",
                "XX XX               E  XX",
                "XXTXXX       XXX  XXX  XX",
                "XX  XXX      XXX  XXX  XX",
                "XX  XXX           XXX  XX",
                "XXX  XX   E       XXX  XX",
                "XXX  XXXXXXX   XXXXXX  XX",
                "XX   XXXXXXXXX   XX    XX",
                "XXXXXXXXXXXXXX  XXX    XX",
                "XX  XXX     XX  XXXXXXXXX",
                "X       XXX             X",
                "XXXXXXXXXXXXXXXXX  XXXXXX",
                "XXXXXXXXXXXXXXX    XXXXXX",
                "XXXXX  XXXXXXX   XXXXXXXX",
                "XXXXX  XXXXXX  XXXXXXXXXX",
                "XXXXXXXXXXXXXX  XXXXXXXXX",
                "XXXXXXXXXXXXXXX  XXXXXXXX",
                "XXXXXXXXXXXXXXX   XXXXXXX",
                "XXXX               XXXXXX",
                "XXXX         E      XXXXX",
                "XXXXXXXXXXXXXXXXXXX  XXXX",
                "XXXXXXXXXXXXXXXXXXXX  TXX",
                "XXXXXXXXXXXXXXXXXXXXXXXXX"
            ]

            treasuress = []

            enemies = []


            levels.append(level_1)
            levels.append(level_2)
            levels.append(level_3)
            levels.append(level_4)

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

                        if character == "E":
                            enemies.append(Enemy(screen_x, screen_y))

                        if character == "T":
                            treasuress.append(treasure(screen_x, screen_y))

            pen = Pen()
            player = Player()

            walls = []

            setup_maze(random.choice(levels))

            turtle.listen()
            turtle.onkey(player.go_left, "Left")
            turtle.onkey(player.go_right, "Right")
            turtle.onkey(player.go_up, "Up")
            turtle.onkey(player.go_down, "Down")
            # if turtle.bye() == True:
            #     import MainMenuV4
            #     MainMenuV4.main_menu()

            wn.tracer(0)

            for enemy in enemies:
                turtle.ontimer(enemy.move, t=250)

            while True:

                for treasure in treasuress:
                    if player.is_collision(treasure):
                        pygame.mixer.pause()
                        outro()
                for enemy in enemies:
                    if player.is_collision(enemy):
                        print ("Player dies!")
                        pygame.mixer.pause()
                        turtle.clearscreen()
                        wn.bgpic(image)
                        game1()
                wn.update()

        def intro():
            turtle.clearscreen()
            test()

        def test():
            wn.tracer(0)
            pen1 = turtle.Pen()

            pen1.color('white')
            wn.bgcolor("Black")
            turtle.clearscreen()

            pen1.up()
            pen1.goto(0, 100)
            pen1.down()
            pen1.write("ello! *instructions* ", False, 'center', font=('Arial', 24, 'bold'))
            turtle.clearscreen()
            wn.bgpic(image)
            introDone = True
            game1()

        def outro():

            import time
            from turtle import Pen
            global mars_game_completed
            pen1 = Pen()

            pen1.color('black', 'green')

            turtle.clearscreen()

            pen1.up()
            pen1.goto(0, 100)
            pen1.down()
            pen1.write("You win! now go, you inglorious bastard!", False, 'center', font=('Arial', 24, 'bold'))
            time.sleep(2)
            turtle.clearscreen()
            # gameDone = True
            turtle.bye()
            pygame.mixer.pause()
            import MainMenuV4
            MainMenuV4.main_menu()

        intro()

    # play the game:
    myGame()
# hisGame()
