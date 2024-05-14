#variables, only positive integers, dont know what happens otherwise
width = 16
height = 16
mines = 40

alive = True
not_mines = ((width * height) - mines)

import pygame
import math
from minesweeper import *
#import time


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
tileFlag = pygame.image.load('Github Repositories/Tillämpad Programmering/Minesweeper/Sprites/TileFlag.png').convert_alpha()
tileMine = pygame.image.load('Github Repositories/Tillämpad Programmering/Minesweeper/Sprites/TileMine.png').convert_alpha()
tileNotMine = pygame.image.load('Github Repositories/Tillämpad Programmering/Minesweeper/Sprites/TileNotMine.png').convert_alpha()



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
			elif board[x][y] == "tileFlag":
				screen.blit(tileFlag, (x*16, y*16))
			elif board[x][y] == "tileMine":
				screen.blit(tileMine, (x*16, y*16))
			elif board[x][y] == "tileNotMine":
				screen.blit(tileNotMine, (x*16, y*16))
			y += 1
		x += 1

def open_square(board_shown, board_hidden, x, y):
	global not_mines
	if board_hidden[x][y] == True:
		board_shown[x][y] = "tileExploded"
		global alive 
		alive = False
		not_mines += 1
		board_shown = loss(board_shown, board_hidden)
	elif board_hidden[x][y] == "0":
		board_shown[x][y] = "tileEmpty"
		board_shown = open_adjacent(board_shown, board_hidden, x, y)
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

	not_mines -= 1
	return board_shown

def open_adjacent(board_shown, board_hidden, x, y):
	width = len(board_shown) - 1
	height = len(board_shown[x]) - 1

	if (x != 0) and (y != 0) and (board_shown[x-1][y-1] == False): #top left
		board_shown = open_square(board_shown, board_hidden, x-1, y-1)
	if (x != 0) and (board_shown[x-1][y] == False): #middle left
		board_shown = open_square(board_shown, board_hidden, x-1, y)
	if (x != 0) and (y != height) and (board_shown[x-1][y+1] == False):# bottom left
		board_shown = open_square(board_shown, board_hidden, x-1, y+1)
	if (y != 0) and (board_shown[x][y-1] == False): #top middle
		board_shown = open_square(board_shown, board_hidden, x, y-1)
	if (y != height) and (board_shown[x][y+1] == False): #bottom middle
		board_shown = open_square(board_shown, board_hidden, x, y+1)
	if (x != width) and (y != 0) and (board_shown[x+1][y-1] == False): #top right
		board_shown = open_square(board_shown, board_hidden, x+1, y-1)
	if (x != width) and (board_shown[x+1][y] == False): #middle right
		board_shown = open_square(board_shown, board_hidden, x+1, y)
	if (x != width) and (y != height) and (board_shown[x+1][y+1] == False):
		board_shown = open_square(board_shown, board_hidden, x+1, y+1)
	return board_shown

def loss(board_shown, board_hidden):
	x = 0
	while x < len(board_shown):
		y = 0
		while y < len(board_shown[x]):
			if (board_shown[x][y] == False) and (board_hidden[x][y] == True):
				board_shown[x][y] = "tileMine"
			if (board_shown[x][y] == "tileFlag") and (not(board_hidden[x][y] == True)):
				board_shown[x][y] = "tileNotMine"
			y += 1
		x += 1
	
	return board_shown

def win(board_shown, board_hidden):
	x = 0
	while x < len(board_shown):
		y = 0
		while y < len(board_shown[x]):
			if (board_shown[x][y] == False) and (board_hidden[x][y] == True):
				board_shown[x][y] = "tileFlag"
			y += 1
		x += 1
	
	return board_shown



def runner(width, height, mines):
	player_board = create_board(height, width)
	hidden_generated = False

	run = True
	global alive
	global not_mines

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
					
				elif ((player_board[pos_x][pos_y]) == False) and (button[0]) and (alive == True):
					#print(hidden_board)
					player_board = open_square(player_board, hidden_board, pos_[0], pos_[1])

				if ((player_board[pos_x][pos_y]) == False) and (button[2]) and (alive == True):
					player_board[pos_x][pos_y] = "tileFlag"

				elif ((player_board[pos_x][pos_y]) == "tileFlag") and (button[2]) and (alive == True):
					player_board[pos_x][pos_y] = False

				elif (((player_board[pos_x][pos_y]) == tile1) or ((player_board[pos_x][pos_y]) == tile2) or ((player_board[pos_x][pos_y]) == tile3) or ((player_board[pos_x][pos_y]) == tile4) or ((player_board[pos_x][pos_y]) == tile5) or ((player_board[pos_x][pos_y]) == tile6) or ((player_board[pos_x][pos_y]) == tile7)) and (button[2]) and (alive == True):
					if ((adjacent_amount(player_board, pos_x, pos_y, "tileFlag")) == 1):
						print("AGGGGGGGGGGGGGGHHHHHHHHHHHH")
						#why no work :(

				if (not_mines == 0):
					win(player_board, hidden_board)

			if event.type == pygame.QUIT:
				run = False

		pygame.display.update()
	pygame.quit

runner(width, height, mines) #width, height, mines




'''
#todo:
4: being able to open adjacent if enough adjacent flags
'''
