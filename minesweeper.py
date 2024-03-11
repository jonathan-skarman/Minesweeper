from random import randint

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

def place_mines(height, width, mines): #sets where the mines are
	i = 0
	board = create_board(height, width)
	while i < mines:
		x = randint(0, width - 1)
		y = randint(0, height - 1)
		if board[x][y] != True:
			board[x][y] = True #if already true
			i += 1
	return board

def generate_nums(board):
	width = len(board) 
	height = len(board[0])

	x = 0
	while x < width:
		y = 0
		while y < height:
			if board[x][y] == False:
				board[x][y] = adjacent_amount(board, x, y)
			y += 1
		x += 1
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


def generate_nums2(board):
	#check top left, and move downward checking one at a time, and replacing it with the number of adjacent
	x = 0
	y = 0
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




#create 2d array (height * width) filled width false
#randomly place (mines) amount of mines
#calculate the numbers for all other spaces (all spaces which are still == false)

def runner(height, width, mines):
	height = 3
	width = 3
	mines = 5

	board = place_mines(height, width, mines)
	#print (board)

	board = generate_nums2(board)
	#print board
	return board



#print (runner(3, 3, 5))

#print (generate_nums2([[False, False, True], [True, False, True], [False, True, True]]))
print (adjacent_amount([[False, False, True], [True, False, True], [False, True, True]], 1, 1))