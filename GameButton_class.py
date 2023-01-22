import pygame

from GameObject_class import GameObject


class GameButton(GameObject):
    def __init__(self, group, animations, size, cords, func, *args, **kwargs):
        super().__init__(group, animations, size, cords, [0, 0])
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def clicked(self):
        self.func(self.args, self.kwargs)

    def update(self, time):
        super().update(time)
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.clicked()


def l(*args, **kwargs):
    print('lol')


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    clock = pygame.time.Clock()
    running = True
    group = pygame.sprite.Group()
    sprite = GameButton(group, {'start': [['pygame-8-1.png'], 2, 8]},
                        [50, 50], [50, 200], l)
    while running:
        screen.fill((255, 255, 255))
        tick = clock.tick(10) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        group.draw(screen)
        group.update(tick)
        pygame.display.flip()
    pygame.quit()
