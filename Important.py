def texts(font, score, color, screen):
    score_text_location = (25, 25)
    score_text = font.render('Score: ' + str(score), 1, color)
    screen.blit(score_text, score_text_location)


def text_objects(text, font, colors):
    textsurface = font.render(text, True, colors)
    return textsurface, textsurface.get_rect()


def button(msg, pos_x, pos_y, width, height, first_color, highlight_color, screen, text_color, action=None):
    import pygame
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if pos_x+width > mouse[0] > pos_x and pos_y+height > mouse[1] > pos_y:
        pygame.draw.rect(screen, highlight_color, (pos_x, pos_y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, first_color, (pos_x, pos_y, width, height))
        small_text = pygame.font.SysFont("algerian", 18)
        text_surf, text_rect = text_objects(msg, small_text, text_color)
        text_rect.center = ((pos_x+(width/2)), (pos_y+(height/2)))
        screen.blit(text_surf, text_rect)
