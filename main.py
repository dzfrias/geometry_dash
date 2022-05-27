import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20, 20))
        self.rect = self.surf.get_rect(center=(250, 250))
        self.surf.fill((0, 255, 0))
        self.vel = [0, 0]
        self.on_ground = True

    def update(self, space, screen):
        if self.ground_collision_detector == True:
            self.on_ground = True
        else:
            self.on_ground = False

        if space and self.on_ground:
            self.vel[1] = -10
            self.on_ground = False

        if self.on_ground and not space:
            self.vel[1] = 0

        if not self.on_ground:
            self.vel[1] += .5

        self.move()

    def move(self):
        self.rect.move_ip(*self.vel)

    def ground_collision_detector(self, platform_group):
        for platform in platform_group:
            if abs(self.rect.bottom-platform.rect.top) in range(1, 15):
                return True
        return False


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(center=(x, y))
        self.surf.fill((255, 255, 0))

    def update(self, dt):
        self.rect.move_ip(-0.175 * dt, 0)


class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.player = Player()
        self.space = False
        self.platform = Platform(50, 20, 600, 250)
        self.ground = Platform(500, 200, 250, 400)

        while self.running:
            self.update()

    def update(self):
        dt = self.clock.tick(30)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                if event.key == K_SPACE:
                    self.space = True
            elif event.type == QUIT:
                self.running = False

        self.player.update(self.space, self.screen)
        self.space = False

        self.screen.fill((100, 110, 110))
        self.screen.blit(self.player.surf, self.player.rect)
        self.platform.update(dt)

        self.screen.fill((100, 110, 110))
        self.screen.blit(self.player.surf, self.player.rect)
        self.screen.blit(self.ground.surf, self.ground.rect)
        self.screen.blit(self.platform.surf, self.platform.rect)
        pygame.display.flip()


if __name__ == "__main__":
    Game()
