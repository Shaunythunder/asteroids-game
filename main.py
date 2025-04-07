import pygame
from constants import * # Everything

def main():
	
	# Pygame start
	pygame.init()

	# Variable definitions
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
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
	
		# Keep this last
		pygame.display.flip()
		

	

if __name__ == "__main__":
	main()
