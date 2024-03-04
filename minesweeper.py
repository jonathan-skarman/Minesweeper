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
		board[randint(0, width - 1)][randint(0, height - 1)] = True #if already true
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
	height = len(board[0]) - 1

	amount = 0
	if (x != 0) and (y != 0) and (board[x-1][y-1]): #top left
		amount += 1
	if (x != 0) and (board[x-1][y]): #middle left
		amount += 1
	if (x != 0) and (y != height) and (board[x-1][y+1]):# bottom left
		amount += 1
	if (y != 0) and (board[x][y-1]): #top middle
		amount += 1
	if (y != height) and (board[x][y+1]): #bottom middle
		amount += 1
	if (x != width) and (y != 0) and (board[x+1][y-1]): #top right
		amount += 1
	if (x != width) and (board[x+1][y]): #middle right
		amount += 1
	if (x != width) and (y != height) and (board[x+1][y+1]):
		amount += 1
	return amount



print(generate_nums(place_mines(5, 5, 5)))

def runner(height, width, mines):
	board = generate_nums(place_mines(height, width, mines))
	opened = create_board(height, width)



height = 5
width = 5
mines = 5
#runner(height, width, mines)