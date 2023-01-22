import os
import sqlite3

import pygame

from GameButton_class import GameButton

ALLOW = '1234567890-_=+qwertyuiopasdfghjklzxcvbnm.,йцукенгшщзхфывапролджэячсмитьбю'
FPS = 60

def db_con(request):
    db = sqlite3.connect('identifier.sqlite')
    sn = db.cursor()
    ret = sn.execute(request)
    db.commit()
    return ret

def font_adr(name):
    return os.path.join('data', 'fonts', name)


def register(screem, Clock):
    running = True
    text = ''
    font = pygame.font.Font(font_adr('Pixel Times.ttf'), 56)
    col = 0

    def stop(*args, **kwargs):
        nonlocal running
        if not text:
            return
        running = False
        db_con(f'INSERT INTO Users(Name) VALUES ("{text}")')


    group = pygame.sprite.Group()
    sprite = GameButton(group, {'start': [['reg_button.png'],
                                          1, 1]}, (6, 900), (150, 500), stop)

    while running:
        text_s = font.render(text, False, 'red')
        screen.fill((220, 180, 200))
        tick = Clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.unicode.lower() in ALLOW and len(text) <= 13:
                text += event.unicode
        if pygame.key.get_pressed()[pygame.K_BACKSPACE] and col == 0:
            text = text[:-1]
            col = 10
        screen.blit(text_s, (100, 400))
        group.draw(screen)
        group.update(tick)
        pygame.display.flip()
        if col > 0:
            col -= 1


def start_screen(screen, clock):
    running = True

    def stop(*args, **kwargs):
        nonlocal running
        running = False

    group = pygame.sprite.Group()
    sprite = GameButton(group, {'start': [['backgrounds', 'Background.png'],
                                          1, 1]}, (600, 900), (0, 0), stop)
    font = pygame.font.Font(font_adr('Pixel Times.ttf'), 64)
    text = font.render('Начать игру', False, 'red')
    while running:
        tick = clock.tick(FPS) / 1000
        screen.fill('red')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        group.update(tick)
        group.draw(screen)
        screen.blit(text, (100, 400))
        pygame.display.flip()


def game(screen, clock):
    running = True
    users_data = db_con('SELECT * from Users').fetchall()
    if not users_data:
        register(screen, clock)


pygame.init()
screen = pygame.display.set_mode((600, 900))
Clock = pygame.time.Clock()
pygame.display.flip()
start_screen(screen, Clock)
game(screen, Clock)
