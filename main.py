import pygame
from constants import * # Everything

def main():
	
	# Pygame start
	pygame.init()

	# Variable definitions
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	dt = 0 #Clock Timer
	
	# Print starting messages
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	# Game loop start
	while True:
		screen.fill("black")
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return
	
		clock.tick(60)
		# Keep this last
		pygame.display.flip()
		
		

	

if __name__ == "__main__":
	main()
