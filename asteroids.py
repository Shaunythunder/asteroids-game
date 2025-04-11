import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, width=2)

    def update(self, dt):
        # Straight line movement
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
    
    def split_on_collision(self):
        # When hit spawn two smaller, faster asteroids. If too small, remove asteroid              
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        spawn_radius = self.radius - ASTEROID_MIN_RADIUS
        spawn_angle = random.uniform(20,50)
        
        spawn_1 = Asteroid(self.position.x, self.position.y, spawn_radius)
        spawn_1_vector = self.velocity.rotate(spawn_angle)
        spawn_1.velocity = spawn_1_vector * 1.2
        
        spawn_2 = Asteroid(self.position.x, self.position.y, spawn_radius)
        spawn_2_vector = self.velocity.rotate(-spawn_angle)
        spawn_2.velocity = spawn_2_vector * 1.2