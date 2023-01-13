import pygame

from GameObject_class import GameObject


class Player(GameObject):
    def __init__(self, group, animations, size, cords,
                 speed_vector):
        super().__init__(group, animations, size, cords, speed_vector)
        self.bool_jump = False
        self.pomenal = False

        self.high_of_jump = 200

    def jump(self, tick):
        if not self.pomenal and self.rect.bottomleft[1] <= self.high_of_jump:
            self.pomenal = True
            self.speed_vector = -90
        elif self.pomenal and self.cords[1] >= self.rect.topleft:
            self.rect.move_ip(*self.cords)
            self.bool_jump = False

    def update(self, time, rotation=0):
        super().update(time, rotation)
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.bool_jump = True
                print('hi')
        if self.bool_jump:
            self.speed_vector = -90
            self.speed_y = 100
            self.jump(time)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    clock = pygame.time.Clock()
    running = True
    group = pygame.sprite.Group()
    sprite = Player(group, ['Player', 'deadpool.png'], [300, 350], [50, 200], [0, 0])
    while running:
        screen.fill((255, 255, 255))
        tick = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        group.draw(screen)
        group.update(tick)
        pygame.display.flip()
    pygame.quit()
