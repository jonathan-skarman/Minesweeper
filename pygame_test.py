import pygame

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('sprite test')

player = pygame.Rect(300, 250, 50, 50)

#VARFÖR FAN BEHÖVER DEN HELA SKITEN, VARFÖR KOLLAR DEN INTE LOKALT
tileUnknown = pygame.image.load('Github Repositories/Tillämpad Programmering/Minesweeper/Sprites/TileUnknown.png').convert_alpha()

run = True
while run:

	screen.fill((50, 50, 50))

	screen.blit(tileUnknown, (0, 0))
	screen.blit(tileUnknown, (16, 0))
	screen.blit(tileUnknown, (0, 16))
	screen.blit(tileUnknown, (16, 16))

	#key = pygame.key.get_pressed()
	#if key[pygame.K_a]:
	#	player.move_ip(-1, 0)
	#elif key[pygame.K_d]:
	#	player.move_ip(1, 0)
	#elif key[pygame.K_w]:
	#	player.move_ip(0, -1)
	#elif key[pygame.K_s]:
	#	player.move_ip(0, 1)

	#pygame.draw.rect(screen, (255, 0, 0), player)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	pygame.display.update()

pygame.quit