import random

import pygame.draw

import constants
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        new_angle = random.uniform(20, 50)

        spliteroid1_speed = self.velocity.rotate(new_angle)
        spliteroid2_speed = self.velocity.rotate(-new_angle)
        spliteroid_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        new_spliteroid1 = Asteroid(self.position.x, self.position.y, spliteroid_radius)
        new_spliteroid1.velocity = spliteroid1_speed * 1.2

        new_spliteroid2 = Asteroid(self.position.x, self.position.y, spliteroid_radius)
        new_spliteroid2.velocity = spliteroid2_speed * 1.2




