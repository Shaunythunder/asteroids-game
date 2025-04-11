import pygame
from constants import * # Everything
from player import *
from asteroids import Asteroid
from asteroidfield import AsteroidField

def main():
	
	# Pygame start
	pygame.init()
	

	# Variable definitions
	clock = pygame.time.Clock()
	dt = 0 #Clock Timer
	
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	asteroid_field = AsteroidField()
	asteroid_objects = pygame.sprite.Group()
	bullet_objects = pygame.sprite.Group()
	drawable_objects = pygame.sprite.Group()
	updatable_objects = pygame.sprite.Group()
	
	Asteroid.containers = (asteroid_objects, updatable_objects, drawable_objects)
	AsteroidField.containers = (updatable_objects,)
	Bullet.containers = (updatable_objects, drawable_objects, bullet_objects)
	Player.containers = (updatable_objects, drawable_objects)
	

	# Print starting messages
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	# Game loop start
	while True:
		screen.fill("black")
		
		for object in drawable_objects:
			object.draw(screen)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return
	
		dt = clock.tick(60)/1000

		updatable_objects.update(dt)

		for asteroid in asteroid_objects:
			if player.check_collision(asteroid):
				print("GAME OVER")
				pygame.quit()
				return
			
		for bullet in bullet_objects:
			for asteroid in asteroid_objects:
				if bullet.check_collision(asteroid):
					asteroid.split()
					bullet.kill()

		# Keep this last
		pygame.display.flip()



if __name__ == "__main__":
	main()
