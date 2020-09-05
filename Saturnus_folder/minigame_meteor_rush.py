saturnus_game_completed = False


def mini_game():

    import pygame
    import random
    import os
    import Important
    from os import path

    img_dir = path.join(path.dirname(__file__), 'img')
    snd_dir = path.join(path.dirname(__file__), 'snd')
    # Constants
    WIDTH = 800
    HEIGHT = 600
    FPS = 60
    SPEED = FPS / 16
    POWERUP_TIME = 5000
    # Colours
    GREEN = (0, 200, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (60, 188, 255)
    CYAN = (0, 232, 215)
    DARKBLUE = (0, 64, 88)
    ORANGE = (248, 120, 88)
    RED = (200, 0, 0)
    PURPLE = (255, 0, 255)
    LIGHTRED = (255, 0, 0)
    LIGHTGREEN = (0, 255, 0)

    # Basic initialization

    pygame.mixer.pre_init(44100, -16, 1, 512)
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Meteor Rush")
    clock = pygame.time.Clock()

    font_name = pygame.font.match_font('algerian')

    def button(msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print(click)
        if x+w > mouse[0] >x and y+h > mouse[1] > y:
            pygame.draw.rect(screen, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                if action == 'quit':
                    pygame.quit()
                    quit()

        else:
            pygame.draw.rect(screen, ic, (x, y, w, h))
            draw_text(screen, msg, 20, (x+(w/2)), ((y-10)+(h/2)))

    def quitgame():
        pygame.mixer.music.stop()
        import MainMenuV4
        MainMenuV4.main_menu()

    def show_finish_screen():
        global saturnus_game_completed
        screen.blit(background, background_rect)
        # pygame.draw.rect(screen, GREEN, (150, 450, 100, 50))
        # pygame.draw.rect(screen, RED, (550, 450, 100, 50))

        draw_text(screen, 'CONGRATULATIONS', 64, WIDTH / 2, HEIGHT / 4)
        draw_text(screen, 'You reached a score of 7500 ', 18, WIDTH / 2, HEIGHT / 2)
        draw_text(screen, 'You got some fuel!! ', 22, WIDTH / 2, HEIGHT / 2.5)
        # draw_text(screen, 'Press any key to begin', 18, WIDTH / 2, HEIGHT * 2 / 3)
        # pygame.display.flip()
        saturnus_game_completed = True

        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            Important.button('PLAY', 150, 500, 100, 50, GREEN, LIGHTGREEN, screen, WHITE, game_loop)
            Important.button('QUIT', 550, 500, 100, 50, RED, LIGHTRED, screen, WHITE, quitgame)
            pygame.display.flip()

    def show_start_screen():

        screen.blit(background, background_rect)
        # pygame.draw.rect(screen, GREEN, (150, 450, 100, 50))
        # pygame.draw.rect(screen, RED, (550, 450, 100, 50))

        draw_text(screen, 'METEOR RUSH', 64, WIDTH / 2, HEIGHT / 4)
        draw_text(screen, 'Arrow keys to move, Space to fire', 16, WIDTH / 2, HEIGHT / 2)
        draw_text(screen, 'Reach a score of 7500 to get Fuel!! ', 16, WIDTH / 2, HEIGHT / 2.5)
        # draw_text(screen, 'Press any key to begin', 18, WIDTH / 2, HEIGHT * 2 / 3)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            Important.button('PLAY', 150, 500, 100, 50, GREEN, LIGHTGREEN, screen, WHITE, game_loop)
            Important.button('QUIT', 550, 500, 100, 50, RED, LIGHTRED, screen, WHITE, quitgame)
            clock.tick(FPS)
            pygame.display.update()

    def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def newmob():
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    def draw_shield_bar(surf, x, y, pct):
        if pct < 0:
            pct = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 10
        fill = (pct / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(surf, CYAN, fill_rect)
        pygame.draw.rect(surf, WHITE, outline_rect, 2)

    def draw_(surf, x, y, pct):
        if pct < 0:
            pct = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 10
        fill = (pct / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(surf, CYAN, fill_rect)
        pygame.draw.rect(surf, WHITE, outline_rect, 2)

    def draw_lives(surf, x, y, lives, img):
        for i in range(lives):
            img_rect = img.get_rect()
            img_rect.x = x + 40 * i
            img_rect.y = y
            surf.blit(img, img_rect)

    # Sprite for the player
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = player_img
            self.rect = self.image.get_rect()
            #self.image.fill(ORANGE)
            self.radius = 27
            self.rect.center = (WIDTH / 2, HEIGHT - 1)
            self.shield = 100
            self.shoot_delay = 250
            self.last_shot = pygame.time.get_ticks()
            self.lives = 3
            self.hidden = False
            self.hide_timer = pygame.time.get_ticks()
            self.power = 1
            self.power_timer = pygame.time.get_ticks()

        def update(self):
            #timeout powerup
            if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
                self.power -= 1
                self.power_time = pygame.time.get_ticks()

            # UNHIDE IF HIDDEN
            if self.hidden and pygame.time.get_ticks() - self.hide_timer > 2000:
                self.hidden = False
                self.rect.centerx = WIDTH / 2
                self.bottom = HEIGHT - 10
            self.speedx = 0
            self.speedy = 0
            # Keypress definitions
            keystate = pygame.key.get_pressed()
            move_left = keystate[pygame.K_LEFT] or keystate[pygame.K_a]
            move_right = keystate[pygame.K_RIGHT] or keystate[pygame.K_d]

            # Movement
            if move_left:
                self.speedx = -8
            if move_right:
                self.speedx = 8
            if keystate[pygame.K_SPACE]:
                self.shoot()
            self.rect.x += self.speedx
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0

            self.rect.y += self.speedy

            # This shit teleports horizontal axis
            if self.rect.left > WIDTH:
                self.rect.right = self.rect.left - WIDTH
            if self.rect.right < 0:
                self.rect.left = self.rect.right + WIDTH
            if self.rect.bottom >= HEIGHT:
                self.rect.bottom = HEIGHT - 32
            if self.rect.top <= 0:
                self.rect.top = 32

        def powerup(self):
            self.power += 1
            self.power_time = pygame.time.get_ticks()

        def shoot(self):
            now = pygame.time.get_ticks()
            if now - self.last_shot > self.shoot_delay:
                self.last_shot = now
                if self.power == 1:
                    bullet = Bullet(self.rect.centerx, self.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    laser1.play()
                if self.power >= 2:
                    bullet1 = Bullet(self.rect.left, self.rect.centery)
                    bullet2 = Bullet(self.rect.right, self.rect.centery)
                    all_sprites.add(bullet1)
                    all_sprites.add(bullet2)
                    bullets.add(bullet1)
                    bullets.add(bullet2)
                    laser1.play()

        def hide(self):
            #hide the player temp
            self.hidden = True
            self.hide_timer = pygame.time.get_ticks()
            self.rect.center = (WIDTH / 2, HEIGHT * 200)

    class Mob(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image_orig = pygame.transform.scale(random.choice(meteor_images), random.choice(meteor_scale_list))
            self.image = self.image_orig.copy()
            self.image_orig.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.radius = int(self.rect.width * .7 / 2)
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(4,8)
            self.speedx = random.randrange(-2, 4)
            self.rot = 0
            self.rot_speed = random.randrange(0, 6)
            self.last_update = pygame.time.get_ticks()
        # Teleports mobs when they pass left side

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

        def update(self):
            self.rotate()
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0 :
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(4,8)
                self.speedx = random.randrange(-2, 4)

    # BULLETS
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(bullet_img, (5, 40))
            #self.image.fill(WHITE)
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.centerx = x
            self.speedy = -12

        def update(self):
            self.rect.y += self.speedy
            # Kill if it moves off the top of screen
            if self.rect.bottom < 0:
                self.kill()

    class Pow(pygame.sprite.Sprite):
        def __init__(self, center):
            pygame.sprite.Sprite.__init__(self)
            self.type = random.choice(['shield', 'gun'])
            self.image = powerup_images[self.type]
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.speedy = 5

        def update(self):
            self.rect.y += self.speedy
            # Kill if it moves off the top of screen
            if self.rect.top > HEIGHT:
                self.kill()

    class Explosion(pygame.sprite.Sprite):
        def __init__(self, center, size):
            pygame.sprite.Sprite.__init__(self)
            self.size = size
            self.image = explosion_anim[self.size][0]
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.frame = 0
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 75

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(explosion_anim[self.size]):
                    self.kill()
                else:
                    center = self.rect.center
                    self.image = explosion_anim[self.size][self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center

    #load images and sounds
    background = pygame.image.load(path.join(img_dir, "background.png")).convert()
    background_rect = background.get_rect()
    player_img = pygame.image.load(path.join(img_dir, 'ship.png')).convert_alpha()
    player_mini_img = pygame.transform.scale(player_img, (32, 32))
    player_mini_img.set_colorkey(BLACK)
    meteor_img = pygame.image.load(path.join(img_dir, "enemy1_1.png")).convert()
    meteor_img1 = pygame.image.load(path.join(img_dir, "enemy2_1.png")).convert()
    meteor_img2 = pygame.image.load(path.join(img_dir, "enemy3_1.png")).convert()
    meteor_img3 = pygame.image.load(path.join(img_dir, "b.png")).convert()
    bullet_img = pygame.image.load(path.join(img_dir, 'laser.png')).convert()
    meteor_images = []
    meteor_list = ["enemy1_1.png", "enemy2_1.png", "enemy3_1.png"]

    #explosion
    explosion_anim = {}
    explosion_anim['lg'] = []
    explosion_anim['sm'] = []
    explosion_anim['player'] = []
    for i in range(9):
        filename = 'regularExplosion0{}.png'.format(i)
        img = pygame.image.load(path.join(img_dir, filename)).convert()
        img.set_colorkey(BLACK)
        img_lg = pygame.transform.scale(img, (75, 75))
        explosion_anim['lg'].append(img_lg)
        img_sm = pygame.transform.scale(img, (32, 32))
        explosion_anim['sm'].append(img_sm)
        filename = 'sonicExplosion0{}.png'.format(i)
        img = pygame.image.load(path.join(img_dir, filename)).convert()
        img.set_colorkey(BLACK)
        explosion_anim['player'].append(img)
    # powerup
    powerup_images = {}
    powerup_images['shield'] = pygame.image.load(path.join(img_dir, 'shield_gold.png')).convert()
    powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'bolt_gold.png')).convert()
    meteor_scales = []
    meteor_scale_list = [(80, 80), (60, 60), (40,40)]
    for img in meteor_list:
        meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())

    #sounds
    laser1 = pygame.mixer.Sound(path.join(snd_dir, 'laser6.wav'))
    player_die_sound = pygame.mixer.Sound(path.join(snd_dir, 'rumble1.ogg'))

    explosion_big = pygame.mixer.Sound(path.join(snd_dir, 'explosion_big.wav'))
    explosion_small = pygame.mixer.Sound(path.join(snd_dir, 'explosion-small.wav'))

    expl_sounds = []
    for snd in ['explosion_big.wav', 'explosion-small.wav']:
        expl_sounds.append(pygame.mixer.Sound(path.join(snd_dir, snd)))
    pygame.mixer.music.load(path.join(snd_dir, 'CH-AY-NA.ogg'))
    pygame.mixer.music.set_volume(0.4)

    shield_sound = pygame.mixer.Sound(path.join(snd_dir, 'pow4.wav'))
    gun_sound = pygame.mixer.Sound(path.join(snd_dir, 'pow5.wav'))

    pygame.mixer.music.play(loops=-1)

    def game_loop():
        global all_sprites
        global mobs
        global bullets
        # Game loop
        game_finished = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(12):
            newmob()
        score = 0
        while True:

            # Keep the pace
            clock.tick(FPS)
            # Process input/events
            for event in pygame.event.get():
                # Key definitions
                keystate = pygame.key.get_pressed()
                # Close window on cross or alt+f4
                if event.type == pygame.QUIT or (keystate[pygame.K_LALT] and keystate[pygame.K_F4]):
                    quitgame()

            # Update
            all_sprites.update()

            # Check collision mob player
            hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
            for hit in hits:
                player.shield -= hit.radius * 1.5
                expl = Explosion(hit.rect.center, 'sm')
                all_sprites.add(expl)
                newmob()
                if player.shield <= 0:
                    player_die_sound.play()
                    death_explosion = Explosion(player.rect.center, 'player')
                    all_sprites.add(death_explosion)
                    player.hide()
                    player.lives -= 1
                    player.shield = 100

            # if player hit powerup
            hits = pygame.sprite.spritecollide(player, powerups, True)
            for hit in hits:
                if hit.type == 'shield':
                    player.shield += random.randrange(10, 30)
                    shield_sound.play()
                    if player.shield >= 100:
                        player.shield = 100
                if hit.type == 'gun':
                    player.powerup()
                    gun_sound.play()
            # if the player died and expl finished then stop
            if player.lives == 0 and not death_explosion.alive():
                show_start_screen()
            if score >= 7500:           # 7500
                game_finished = True
            if game_finished:
                show_finish_screen()

            # Check collission mob bullet
            hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
            for hit in hits:
                score += 50 - hit.radius
                random.choice(expl_sounds).play()
                expl = Explosion(hit.rect.center, 'lg')
                all_sprites.add(expl)
                if random.random() > 0.97:
                    pow = Pow(hit.rect.center)
                    all_sprites.add(pow)
                    powerups.add(pow)
                newmob()

            # Draw/render
            screen.fill(DARKBLUE)
            screen.blit(background, background_rect)
            all_sprites.draw(screen)
            draw_text(screen, str(score), 25, WIDTH / 2, 10)
            draw_shield_bar(screen, 5, 5, player.shield)
            draw_lives(screen, WIDTH - 150, 5, player.lives, player_mini_img)
            # 'Flip' the display after drawing everything
            pygame.display.flip()

    # print('start screen')
    show_start_screen()
    # # Game loop
    # game_finished = False
    # game_over = True
    # running = True
    # while running:
    #     if game_over:
    #         show_start_screen()
    #         game_over = False
    #         all_sprites = pygame.sprite.Group()
    #         mobs = pygame.sprite.Group()
    #         bullets = pygame.sprite.Group()
    #         powerups = pygame.sprite.Group()
    #         player = Player()
    #         all_sprites.add(player)
    #         for i in range(12):
    #             newmob()
    #         score = 0
    #
    #     # Keep the pace
    #     clock.tick(FPS)
    #     # Process input/events
    #     for event in pygame.event.get():
    #         # Key definitions
    #         keystate = pygame.key.get_pressed()
    #         # Close window on cross or alt+f4
    #         if event.type == pygame.QUIT or (keystate[pygame.K_LALT] and keystate[pygame.K_F4]):
    #             running = False
    #
    #     # Update
    #     all_sprites.update()
    #
    #     # Check collision mob player
    #     hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    #     for hit in hits:
    #         player.shield -= hit.radius * 1.5
    #         expl = Explosion(hit.rect.center, 'sm')
    #         all_sprites.add(expl)
    #         newmob()
    #         if player.shield <= 0:
    #             player_die_sound.play()
    #             death_explosion = Explosion(player.rect.center, 'player')
    #             all_sprites.add(death_explosion)
    #             player.hide()
    #             player.lives -= 1
    #             player.shield = 100
    #
    #     # if player hit powerup
    #     hits = pygame.sprite.spritecollide(player, powerups, True)
    #     for hit in hits:
    #         if hit.type == 'shield':
    #             player.shield += random.randrange(10, 30)
    #             shield_sound.play()
    #             if player.shield >= 100:
    #                 player.shield = 100
    #         if hit.type == 'gun':
    #             player.powerup()
    #             gun_sound.play()
    #     # if the player died and expl finished then stop
    #     if player.lives == 0 and not death_explosion.alive():
    #         game_over = True
    #     if score >= 7500:
    #         game_finished = True
    #     if game_finished:
    #         show_finish_screen()
    #
    #     # Check collission mob bullet
    #     hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    #     for hit in hits:
    #         score += 50 - hit.radius
    #         random.choice(expl_sounds).play()
    #         expl = Explosion(hit.rect.center, 'lg')
    #         all_sprites.add(expl)
    #         if random.random() > 0.97:
    #             pow = Pow(hit.rect.center)
    #             all_sprites.add(pow)
    #             powerups.add(pow)
    #         newmob()
    #
    #     # Draw/render
    #     screen.fill(DARKBLUE)
    #     screen.blit(background, background_rect)
    #     all_sprites.draw(screen)
    #     draw_text(screen, str(score), 25, WIDTH / 2, 10)
    #     draw_shield_bar(screen, 5, 5, player.shield)
    #     draw_lives(screen, WIDTH - 150, 5, player.lives, player_mini_img)
    #     # 'Flip' the display after drawing everything
    #     pygame.display.flip()

# print('minigame')
# mini_game()


