import pygame
import random
import os
from os import path
os.environ["SDL_VIDEO_CENTERED"] = "1"

# Asset folder specification
img_dir = path.join(path.dirname(__file__), 'img')
sfx_dir = path.join(path.dirname(__file__), 'sfx')

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60
# Speed influences mob/player/level speed
SPEED = 4
SPAWN = 16
HITBOX = 0.85
LIFE = 5

# Global vars
life = 0

# mainmenu var
neptune_game_completed = False

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (60, 188, 255)
CYAN = (0, 232, 215)
DARKBLUE = (0, 64, 88)
ORANGE = (248, 120, 88)
RED = (168, 16, 0)
PURPLE = (255, 0, 255)

# Basic initialization
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fuel Flight | Alpha3")
clock = pygame.time.Clock()

# sfx
pygame.mixer.music.load(path.join(sfx_dir, 'gameLoop2.wav'))
pygame.mixer.music.play(-1)

# Set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = path.join(game_folder, "img")

# Load all game gfx
background = pygame.image.load(path.join(img_dir, "neptune.jpg")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "attackShip32.GIF"))
mob_img = pygame.image.load(path.join(img_dir, "mobBox.GIF"))

# Load SFX
hit_sound = []
for snd in ['hurt1.wav', 'hurt2.wav']:
    hit_sound.append(pygame.mixer.Sound(path.join(sfx_dir, snd)))

# font_name = pygame.font.Font('algerian.ttf', 18)
font_name = pygame.font.match_font('algerian')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


# Sprite for the player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (64, 32))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 4)
        # pygame.draw.circle(self.image, WHITE, self.rect.center, int(self.radius))
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    #     self.rot = 0
    #     self.rot_speed = random.randrange(SPEED / 2, SPEED)
    #     self.last_update = pygame.time.get_ticks()
    #
    # def rotate(self):
    #     now = pygame.time.get_ticks()
    #     if now - self.last_update > 50:
    #         self.last_update = now
    #         self.rot = (self.rot + self.rot_speed) % 360
    #         self.image = pygame.transform.rotate(self.image_orig, self.rot)

    def update(self):
        # self.rotate()
        self.speedx = 0
        self.speedy = 0
        movement_speed = SPEED
        boost = SPEED
        # Keypress definitions
        keystate = pygame.key.get_pressed()
        move_up = keystate[pygame.K_UP] or keystate[pygame.K_w]
        move_down = keystate[pygame.K_DOWN] or keystate[pygame.K_s]
        move_left = keystate[pygame.K_LEFT] or keystate[pygame.K_a]
        move_right = keystate[pygame.K_RIGHT] or keystate[pygame.K_d]
        shift_key = keystate[pygame.K_LSHIFT] or keystate[pygame.K_RSHIFT]
        # Movement
        if move_left:
            self.speedx -= movement_speed
        if move_right:
            self.speedx += movement_speed
        if move_up:
            self.speedy -= movement_speed
        if move_down:
            self.speedy += movement_speed
        # Boost bound to LSHIFT
        if shift_key and move_left:
            self.speedx -= boost
        if shift_key and move_right:
            self.speedx += boost
        if shift_key and move_up:
            self.speedy -= boost
        if shift_key and move_down:
            self.speedy += boost
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # This shit teleports horizontal axis
        if self.rect.left > WIDTH:
            self.rect.right = self.rect.left - WIDTH
        if self.rect.right < 0:
            self.rect.left = self.rect.right + WIDTH
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT - self.rect.height
        if self.rect.top <= 0:
            self.rect.top = self.rect.height

    def shoot(self):
        bullet = Bullet(self.rect.right, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(mob_img, (32, 32))
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 2 * 0.85)
        pygame.draw.circle(self.image, RED, self.rect.center, int(self.radius))
        # # TESTING SPAWN IN ROW MID SCREEN
        # self.rect.y = random.randrange(int((HEIGHT) / 2 - 32 * 2, int(HEIGHT) / 2 + 32 * 2, 32)
        # self.rect.x = random.randrange(int(WIDTH) + self.rect.width, int(WIDTH) + self.rect.width * SPAWN, self.rect.width)
        self.rect.y = random.randrange(0 + self.rect.height, HEIGHT - self.rect.height, self.rect.height * 2)
        self.rect.x = random.randrange(WIDTH, WIDTH + WIDTH + self.rect.width * (WIDTH % SPAWN), self.rect.width * 2)
        self.speedx = SPEED
        # self.speedy = random.randrange(8 // -2, 8 // 16)
        self.rot = 0
        self.rot_speed = random.randrange(SPEED / 4, SPEED * 2)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    # Teleports mobs when they pass left side
    def update(self):
        self.rotate()
        self.rect.x -= self.speedx
        # self.rect.y += self.speedy
        if self.rect.right < 0 or self.rect.right == 0:
            # # TESTING SPAWN IN ROW MID SCREEN
            # self.rect.y = random.randrange(int(HEIGHT) / 2 - self.rect.height * 2, int(HEIGHT) / 2 + self.rect.height * 2, self.rect.height)
            # self.rect.x = random.randrange(int(WIDTH) + self.rect.width, int(WIDTH) + self.rect.width * SPAWN, self.rect.width)
            self.rect.y = random.randrange(0 + self.rect.height, HEIGHT - self.rect.height, self.rect.height * 2)
            self.rect.x = WIDTH + self.rect.width

# class Background(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.speedx = 1


"""class Staticmob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(self.rect.height, int(HEIGHT) - self.rect.width)
        self.rect.x = random.randrange(int(WIDTH) + self.rect.width, int(WIDTH) + 320)
        self.speedx = int(SPEED)
        # self.speedy = random.randrange(int(SPEED) / -16, int(SPEED) / 16)
    # Teleports mobs when they pass left side
    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < 0 - 16 or self.rect.top > HEIGHT or self.rect.bottom < 0:
            self.rect.y = random.randrange(self.rect.height, int(HEIGHT) - self.rect.width)
            self.rect.x = random.randrange(int(WIDTH) + self.rect.width, int(WIDTH) + 320)"""


# GO screen
def show_go_screen():
    screen.fill(BLACK)
    if deaths > 0:
        draw_text(screen, 'Your ship is toast!', 32, WIDTH / 2, HEIGHT / 4)
    else:
        draw_text(screen, 'You spot a fueling station just off Neptune', 21, WIDTH / 2, HEIGHT / 4)
        draw_text(screen, 'Navigate to its center for the fuel to reach Eden!', 21, WIDTH / 2, HEIGHT / 4 + 21 * 1.5)
    draw_text(screen, 'Arrow keys / WASD to move, evade the debris', 18, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, 'Press SPACE to begin', 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                waiting = False


# BULLETS
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32,16))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.centery = y
        self.speedx = SPEED // 0.5

    def update(self):
        self.rect.x += self.speedx
        # Kill if it moves off the top of screen
        if self.rect.left > WIDTH:
            self.kill()


# Sprite call
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
staticmobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
# player = Player()
# all_sprites.add(player)
#
# for i in range(SPAWN):
#     m = Mob()
#     all_sprites.add(m)
#     mobs.add(m)

# for i in range(12):
#     s = Staticmob()
#     all_sprites.add(s)
#     staticmobs.add(s)

# Game loop
running = True
game_over = True
deaths = 0


def game_loop():
    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()

    # bullets = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    for i in range(SPAWN):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    global game_over
    global life
    global running
    global hit
    global deaths

    life = 0
    while True:
        if game_over:
            show_go_screen()
            game_over = False

        # Keep the pace
        clock.tick(FPS)

        # Process input/events
        for event in pygame.event.get():
            # Key definitions
            keystate = pygame.key.get_pressed()

            # Close window on cross or alt+f4
            if event.type == pygame.QUIT or (keystate[pygame.K_LALT] and keystate[pygame.K_F4]):
                running = False

        # # Bullet fire
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         player.shoot()

            pygame.init()
        # Update
        all_sprites.update()

        # Check collision mob player
        crash = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
        if crash:
            random.choice(hit_sound).play()
            life += 1
            if life == LIFE:
                deaths += 1
                game_over = True
                game_loop()

                # life = 0


        # Check collission
        bullseye = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in bullseye:
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)

        life_score = LIFE - life
        # Draw/render
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, 'Life: ' + str(life_score), 18, WIDTH - 64, 64)

        # 'Flip' the display after drawing everything
        pygame.display.flip()


game_loop()


# while running:
#     if game_over:
#         show_go_screen()
#         game_over = False
#
#     # Keep the pace
#     clock.tick(FPS)
#
#     # Process input/events
#     for event in pygame.event.get():
#         # Key definitions
#         keystate = pygame.key.get_pressed()
#
#         # Close window on cross or alt+f4
#         if event.type == pygame.QUIT or (keystate[pygame.K_LALT] and keystate[pygame.K_F4]):
#             running = False
#
#         # Bullet fire
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 player.shoot()
#
#         pygame.init()
#     # Update
#     all_sprites.update()
#
#     # Check collision mob player
#     crash = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
#     if crash:
#         random.choice(hit_sound).play()
#         life += 1
#         if life == LIFE:
#             game_over = True
#             life = 0
#             deaths += 1
#
#     # Check collission
#     bullseye = pygame.sprite.groupcollide(mobs, bullets, True, True)
#     for hit in bullseye:
#         m = Mob()
#         all_sprites.add(m)
#         mobs.add(m)
#
#     life_score = LIFE - life
#     # Draw/render
#     screen.blit(background, background_rect)
#     all_sprites.draw(screen)
#     draw_text(screen, 'Life: ' + str(life_score), 18, WIDTH - 64, 64)
#
#     # 'Flip' the display after drawing everything
#     pygame.display.flip()
