import datetime
import json
import os
from random import randint

import pygame

from GameObject_class import GameObject
from Backgroung_class import Backgroung
from GameButton_class import GameButton
from coin import Coin
from player_class import Player

ALLOW = '1234567890-_=+qwertyuiopasdfghjklzxcvbnm.,йцукенгшщзхфывапролджэячсмитьбю'
fps = 24
Name = ''
Money = 0
move = -24 * 5


def m():
    global Money
    Money += 1


def register(screem, Clock):
    running = True
    text = ''
    font = pygame.font.Font(font_adr('Pixel Times.ttf'), 56)
    col = 0

    def stop(*args, **kwargs):
        nonlocal running
        global Name
        if not text:
            return
        running = False
        Name = text

    group = pygame.sprite.Group()
    sprite = GameButton(group, {'start': [['reg_button.png'],
                                          1, 1]}, (6, 900), (150, 500), stop)

    while running:
        text_s = font.render(text, False, 'red')
        screen.fill((220, 180, 0))
        tick = Clock.tick(fps) / 1000
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


def font_adr(name):
    return os.path.join('data', 'fonts', name)


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
        tick = clock.tick(fps) / 1000
        screen.fill('red')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        group.update(tick)
        group.draw(screen)
        screen.blit(text, (100, 400))
        pygame.display.flip()


def game(screen, clock):
    global fps, move

    def open_invent(*args, **kwargs):
        nonlocal menu
        menu = True

    def fast_move(*args, **kwargs):
        global fps, move
        nonlocal coin_speed, fon
        if move == -24 * 5:
            fps = 48
            move = 48 * 10
            coin_speed = 400
            fon.init_vector((-180, 400))

    running = True
    coin_speed = 200
    menu = False
    menu_group = pygame.sprite.Group()
    menu = GameObject(menu_group, {'start': [['menu.png'], 1, 1]}, (0, 0), (0, 0), (0, 0))
    font = pygame.font.Font(font_adr('Pixel Times.ttf'), 24)
    main_group = pygame.sprite.Group()
    fon = Backgroung(main_group, {'start': [['backgrounds', 'gr.png'], 1, 1]}, (0, 0), (0, 0), (180, 200))
    player = Player(main_group, {'start': [['Player', 'player.png'], 1, 5]}, (0, 0), (30, 430), (0, 0))
    money_group = pygame.sprite.Group()
    fast_btn = GameButton(main_group, {'start': [['fast.xcf'], 1, 1]},
                          (1, 1), (0, 670), fast_move)
    inventory_btn = GameButton(main_group, {'start': [['invent2_scaled.xcf'], 1, 1]},
                               (1, 1), (100, 620), open_invent)
    col = 0

    while running:
        if not col:
            [Coin(money_group, {'start': [['pygame-8-1.png'], 2, 8]}, (randint(900, 1000), randint(200, 600)),
                  (-180, coin_speed), player, m) for _ in range(randint(0, 10))]
            col = randint(24, 120)
        else:
            col -= 1
        screen.fill('white')
        tick = clock.tick(fps) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        main_group.draw(screen)
        main_group.update(tick)
        money_group.draw(screen)
        money_group.update(tick)
        screen.blit(font.render(f'Монеты: {Money}', False, 'red'), (0, 0))
        pygame.display.flip()
        if move == 0:
            fps = 24
            coin_speed = 200
            fon.init_vector((-180, 200))
        if move > -24 * 5:
            move -= 1
        print(move)


pygame.init()
screen = pygame.display.set_mode((600, 900))
Clock = pygame.time.Clock()
pygame.display.flip()
start_screen(screen, Clock)
if not os.path.exists('data.json'):
    data = open('data.json', 'w')
    register(screen, Clock)
    start_dict = {'last_time': str(datetime.datetime.now()),
                  'Name': Name,
                  'Money': 0,
                  'weapon-1 level': 0,
                  'weapon-2 level': 0,
                  'weapon-3 level': 0,
                  'money per second': 0
                  }
    data.write(json.dumps(start_dict))
    data.close()
data = json.loads(open('data.json', 'r').read())
Money = data['Money']
Name = data['Name']
game(screen, Clock)
data = open('data.json', 'w')
start_dict = {'last_time': str(datetime.datetime.now()),
              'Name': Name,
              'Money': Money,
              'weapon-1 level': 0,
              'weapon-2 level': 0,
              'weapon-3 level': 0,
              'money per second': 0
              }
data.write(json.dumps(start_dict))
data.close()
