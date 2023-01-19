import pygame

from GameObject_class import GameObject


class Enemy(GameObject):
    def __init__(self, group, animations, size, cords, hp):
        super().__init__(group, animations, size, cords, (180, 200))

        self.hp = hp

    def update(self, time):
        super().update(time)
        if self.hp <= 0 and self.rect.topright[0] < 0:
            self.kill()
            print('I am dead')

    def damage(self, damage):
        self.hp -= damage


pygame.init()
group = pygame.sprite.Group()
enemy1 = Enemy(group, ['Player', 'deadpool.png'], (300, 350), (600, 350), 300)
screen = pygame.display.set_mode((300, 500))
clock = pygame.time.Clock()
running = True
while running:
    enemy1.damage(1)
    screen.fill((255, 255, 255))
    tick = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    group.draw(screen)
    group.update(tick)
    pygame.display.flip()
pygame.quit()
