import pygame
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius)
 
    def update(self, dt):
        self.position += pygame.Vector2(0,1) + self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20,50)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        velocity_one = self.velocity.rotate(angle)
        velocity_two = self.velocity.rotate(-angle)

        ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast_2 = Asteroid(self.position.x, self.position.y, new_radius)

        ast_1.velocity = velocity_one * 1.2
        ast_2.velocity = velocity_two * 1.2

