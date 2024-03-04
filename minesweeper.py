height = 5
width = 5
mines = 5

def create_column(length): #creates a column of "False" that is length long
	i = 0
	column = []
	while i < length:
		column.append(False)
		i += 1
	return column

def create_board(height, width):
	i = 0
	board = []
	while i < width:
		board.append(create_column(height))
		i += 1
	return board
