import pygame

# Define class for circle hitboxes
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def check_collision(self, circle_object):
        collision_radius = self.radius + circle_object.radius
        if collision_radius >= self.position.distance_to(circle_object.position):
            return True
        return False