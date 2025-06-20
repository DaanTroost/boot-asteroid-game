import pygame
import constants
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            self.rotate(360 - dt)
        if keys[pygame.K_f]:
            self.rotate(dt)
        if keys[pygame.K_e]:
            self.move(dt)
        if keys[pygame.K_d]:
            self.move(-dt)
        if keys[pygame.K_BACKSPACE]:
            self.shoot()

        self.timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return
        bullet = Shot(self.position.x, self.position.y)
        start = pygame.Vector2(0, 1).rotate(self.rotation)
        bullet.velocity = start * constants.PLAYER_SHOOT_SPEED
        self.timer = constants.PLAYER_SHOT_COOLDOWN


