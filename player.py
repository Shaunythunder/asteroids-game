import pygame
from circleshape import CircleShape
from constants import * # Everything

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # Logic for creating player shape
    def player_triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # Logic for drawing on screen
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.player_triangle(), 2)
    

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate_left(dt)

        if keys[pygame.K_d]:
            self.rotate_right(dt)

        if keys[pygame.K_w]:
            self.move_forward(dt)

        if keys[pygame.K_s]:
            self.move_backward(dt)

        if keys[pygame.K_SPACE]:
            if self.timer < 0:
                self.timer = PLAYER_SHOT_COOLDOWN
                self.shoot()


    def move_forward(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVEMENT_SPEED * dt

    def move_backward(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVEMENT_SPEED * -dt

    def rotate_left(self, dt):
        self.rotation += PLAYER_TURN_SPEED * -dt

    def rotate_right(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self):
        shot = Bullet(self.position.x, self.position.y, PLAYER_SHOT_RADIUS)
        direction = pygame.Vector2(1, 0)
        rotated_direction = direction.rotate(self.rotation + 90)
        shot.velocity = rotated_direction * PLAYER_SHOOT_SPEED

class Bullet(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, width=2)

    def update(self, dt):
        # Straight line movement
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt