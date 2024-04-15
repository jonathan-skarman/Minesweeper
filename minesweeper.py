from random import randint
import pygame

def create_column(length): #creates a column of "False" that is length long
	i = 0
	column = []
	while i < length:
		column.append(False)
		i += 1
	return column

def create_board(height, width): #creates a board with only false
	i = 0
	board = []
	while i < width:
		board.append(create_column(height))
		i += 1
	return board

def place_mines(height, width, mines, x, y): #sets where the mines are
	i = 0
	board = create_board(height, width)
	while i < mines:
		x_ = randint(0, width - 1)
		y_ = randint(0, height - 1)

		#makes sure tile clicked and adjacent are safe, and current tile isn't a mine
		if (not((x_ == x) or (x_ == x -1) or (x_ == x +1) or (y_ == y) or (y_ == y -1) or (y_ == y +1))) and (not(board[x_][y_] == True)):
			board[x_][y_] = True #if already true
			i += 1
	return board

def adjacent_amount(board, x, y):
	width = len(board) - 1
	height = len(board[x]) - 1

	amount = 0
	if (x != 0) and (y != 0) and (board[x-1][y-1] == True): #top left
		amount += 1
	if (x != 0) and (board[x-1][y] == True): #middle left
		amount += 1
	if (x != 0) and (y != height) and (board[x-1][y+1] == True):# bottom left
		amount += 1
	if (y != 0) and (board[x][y-1] == True): #top middle
		amount += 1
	if (y != height) and (board[x][y+1] == True): #bottom middle
		amount += 1
	if (x != width) and (y != 0) and (board[x+1][y-1] == True): #top right
		amount += 1
	if (x != width) and (board[x+1][y] == True): #middle right
		amount += 1
	if (x != width) and (y != height) and (board[x+1][y+1] == True):
		amount += 1
	return amount


def generate_nums(board):
	x = 0
	#print (len(board))

	while x < len(board):
		y = 0
		while y < len(board[x]):
			#print (x)
			if board[x][y] == False:
				board[x][y] = adjacent_amount(board, x, y)
			y += 1
		x += 1

	return board

def generate_num_outOfPlace(board):
	newBoard = []
	x = 0

	while x < len(board):
		newBoard.append([])
		y = 0
		while y < len(board[x]):
			if board[x][y] == False:
				newBoard[x].append(str(adjacent_amount(board, x, y)))
			else:
				newBoard[x].append(True)
			y += 1
		x += 1

	return newBoard




#create 2d array (height * width) filled width false
#randomly place (mines) amount of mines
#calculate the numbers for all other spaces (all spaces which are still == false)

def runner(height, width, mines):
	board = place_mines(height, width, mines)
	#print (board)

	board = generate_num_outOfPlace(board)
	#print board
	return board



#print (runner(5, 5, 5))

#print (generate_num_outOfPlace([[False, False, True], [True, False, True], [False, True, True]]))
#print (adjacent_amount([[False, False, True], [True, False, True], [False, True, True]], 1, 1))
