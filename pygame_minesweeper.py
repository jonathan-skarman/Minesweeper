#variables, only positive integers, dont know what happens otherwise
width = 7
height = 7
mines = 5

import pygame
import math
from minesweeper import *

pygame.init()
screen_width = width * 16
screen_height = height * 16
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Minesweeper')

#sprites
tileUnknown = pygame.image.load('Github Repositories/Tillämpad Programmering/Minesweeper/Sprites/TileUnknown.png').convert_alpha()
tileExploded = pygame.image.load('Github Repositories/Tillämpad Programmering/Minesweeper/Sprites/TileExploded.png').convert_alpha()
tileEmpty = pygame.image.load('Github Repositories/Tillämpad Programmering/Minesweeper/Sprites/TileEmpty.png').convert_alpha()
tile1 = pygame.image.load('Github Repositories/Tillämpad Programmering/Minesweeper/Sprites/Tile1.png').convert_alpha()
tile2 = pygame.image.load('Github Repositories/Tillämpad Programmering/Minesweeper/Sprites/Tile2.png').convert_alpha()
tile3 = pygame.image.load('Github Repositories/Tillämpad Programmering/Minesweeper/Sprites/Tile3.png').convert_alpha()
tile4 = pygame.image.load('Github Repositories/Tillämpad Programmering/Minesweeper/Sprites/Tile4.png').convert_alpha()
tile5 = pygame.image.load('Github Repositories/Tillämpad Programmering/Minesweeper/Sprites/Tile5.png').convert_alpha()
tile6 = pygame.image.load('Github Repositories/Tillämpad Programmering/Minesweeper/Sprites/Tile6.png').convert_alpha()
tile7 = pygame.image.load('Github Repositories/Tillämpad Programmering/Minesweeper/Sprites/Tile7.png').convert_alpha()
tile8 = pygame.image.load('Github Repositories/Tillämpad Programmering/Minesweeper/Sprites/Tile8.png').convert_alpha()



#functions
def draw_board(board):
	x = 0
	while x < len(board):
		y = 0
		while y < len(board[x]):
			if board[x][y] == False:
				screen.blit(tileUnknown, (x*16, y*16))
			elif board[x][y] == "tileExploded":
				screen.blit(tileExploded, (x*16, y*16))
			elif board[x][y] == "tileEmpty":
				screen.blit(tileEmpty, (x*16, y*16))
			elif board[x][y] == "tile1":
				screen.blit(tile1, (x*16, y*16))
			elif board[x][y] == "tile1":
				screen.blit(tile1, (x*16, y*16))
			elif board[x][y] == "tile2":
				screen.blit(tile2, (x*16, y*16))
			elif board[x][y] == "tile3":
				screen.blit(tile3, (x*16, y*16))
			elif board[x][y] == "tile4":
				screen.blit(tile4, (x*16, y*16))
			elif board[x][y] == "tile5":
				screen.blit(tile5, (x*16, y*16))
			elif board[x][y] == "tile6":
				screen.blit(tile6, (x*16, y*16))
			elif board[x][y] == "tile7":
				screen.blit(tile7, (x*16, y*16))
			elif board[x][y] == "tile8":
				screen.blit(tile8, (x*16, y*16))
			y += 1
		x += 1

def open_square(board_shown, board_hidden, x, y):
	if board_hidden[x][y] == True:
		board_shown[x][y] = "tileExploded"
	elif board_hidden[x][y] == "0":
		board_shown[x][y] = "tileEmpty"
	elif board_hidden[x][y] == "1":
		board_shown[x][y] = "tile1"
	elif board_hidden[x][y] == "2":
		board_shown[x][y] = "tile2"
	elif board_hidden[x][y] == "3":
		board_shown[x][y] = "tile3"
	elif board_hidden[x][y] == "4":
		board_shown[x][y] = "tile4"
	elif board_hidden[x][y] == "5":
		board_shown[x][y] = "tile5"
	elif board_hidden[x][y] == "6":
		board_shown[x][y] = "tile6"
	elif board_hidden[x][y] == "7":
		board_shown[x][y] = "tile7"
	elif board_hidden[x][y] == "8":
		board_shown[x][y] = "tile8"

	return board_shown



def runner(width, height, mines):
	player_board = create_board(height, width)
	hidden_generated = False

	run = True
	while run:
		#updates background, 
		screen.fill((50, 50, 50))

		draw_board(player_board)

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				button = pygame.mouse.get_pressed()

				pos_ = [math.floor(pos[0]/16), math.floor(pos[1]/16)]
				pos_x = int(pos_[0])
				pos_y = int(pos_[1])
				
				#pos / 16 rounded down gives what tile has been clicked


				if (not(hidden_generated)) and (button[0]): #if hidden isn't generated and left mouse is clicked
					hidden_board = generate_num_outOfPlace(place_mines(height, width, mines, pos_[0], pos_[1]))
					player_board = open_square(player_board, hidden_board, pos_[0], pos_[1])
					hidden_generated = True

				#if the clicked position isn't opened yet
				#if player_board[pos[0]/16, pos[1]/16] == False:
					
				elif ((player_board[pos_x][pos_y]) == False) and (button[0]):
					print(hidden_board)
					player_board = open_square(player_board, hidden_board, pos_[0], pos_[1])

				#print(hidden_board)

			if event.type == pygame.QUIT:
				run = False

		pygame.display.update()
	pygame.quit

	#check first opened space and set that space, and adjacent to not be able to be mines
	#generate board, both hidden and to show the player
	#check where they move and open / flag
	#if all mines are flagged they win

runner(width, height, mines) #width, height, mines