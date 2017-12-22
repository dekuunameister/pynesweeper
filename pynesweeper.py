#!/usr/bin/env python3

from random import randint, randrange
from copy import deepcopy

def make_board(width, height, num_mines):
	""" Makes the board and the board the user sees. """
	board = []
	proxy_board = []
	row = []
	proxy_row = []
	for i in range(height):
		for j in range(width):
			proxy_row.append('_')
		proxy_board.append(proxy_row)
		proxy_row = []

	for i in range(height):
		for j in range(width):
			row.append('_')
		board.append(row)
		row = []

	# popoulate the board with mines
	for i in range(num_mines):
		print('adsfa')
		rand_1st = randrange(0, height)
		rand_2nd = randrange(0, width)

		# keep picking spaces to be mines if you repeated an index
		while board[rand_1st][rand_2nd] != '_':
			rand_1st = randrange(0, height)
			rand_2nd = randrange(0, width)

		board[rand_1st][rand_2nd] = '*'

	""" Check the mines touching each of the 4 corner tiles. """
	# upper left corner
	if board[0][0] != '*':
		mines = 0
		if board[1][0] == '*':
			mines += 1
		if board[0][1] == '*':
			mines += 1
		if board[1][1] == '*':
			mines += 1
		board[0][0] = str(mines)
	# lower left corner
	if board[height-1][0] != '*':
		mines = 0
		if board[height-1][1] == '*':
			mines += 1
		if board[height-2][0] == '*':
			mines += 1
		if board[height-2][1] == '*':
			mines += 1
		board[height-1][0] = str(mines)
	# upper right corner
	if board[0][width-1] != '*':
		mines = 0
		if board[0][width-2] == '*':
			mines += 1
		if board[1][width-1] == '*':
			mines += 1
		if board[1][width-2] == '*':
			mines += 1
		board[0][width-1] = str(mines)
	# lower right corner
	if board[height-1][width-1] != '*':
		mines = 0
		if board[height-2][width-1] == '*':
			mines += 1
		if board[height-1][width-2] == '*':
			mines += 1
		if board[height-2][width-2] == '*':
			mines += 1
		board[height-1][width-1] = str(mines)

	""" Check the number of mines touching the edges. """
	# left edge
	for i in range(1, height-1):
		if board[i][0] != '*':
			mines = 0
			if board[i+1][0] == '*':
				mines += 1
			if board[i-1][0] == '*':
				mines += 1
			if board[i][1] == '*':
				mines += 1
			if board[i-1][1] == '*':
				mines += 1
			if board[i+1][1] == '*':
				mines += 1
			board[i][0] = str(mines)

	# top edge
	for j in range (1, width-1):
		if board[0][j] != '*':
			mines = 0
			if board[0][j+1] == '*':
				mines += 1
			if board[0][j-1] == '*':
				mines += 1
			if board[1][j] == '*':
				mines += 1
			if board[1][j-1] == '*':
				mines += 1
			if board[1][j+1] == '*':
				mines += 1
			board[0][j] = str(mines)

	# right edge
	j = width - 1
	for i in range(1, height-1):
		if board[i][j] != '*':
			mines = 0
			if board[i][j-1] == '*':
				mines += 1
			if board[i-1][j] == '*':
				mines += 1
			if board[i+1][j] == '*':
				mines += 1
			if board[i-1][j-1] == '*':
				mines += 1
			if board[i+1][j-1] == '*':
				mines += 1
			board[i][j] = str(mines)

	# bottom edge
	i = height - 1
	for j in range(1, width-1):
		if board[i][j] != '*':
			mines = 0
			if board[i][j-1] == '*':
				mines += 1
			if board[i][j+1] == '*':
				mines += 1
			if board[i-1][j-1] == '*':
				mines += 1
			if board[i-1][j+1] == '*':
				mines += 1
			if board[i-1][j] == '*':
				mines += 1
			board[i][j] = str(mines)

	""" Check the number of mines touching the middle tiles. """
	for i in range (1, height-1):
		for j in range(1, width-1):
			if board[i][j] != '*':
				mines = 0
				if board[i-1][j] == '*':
					mines += 1
				if board[i][j-1] == '*':
					mines += 1
				if board[i][j+1] == '*':
					mines += 1
				if board[i+1][j] == '*':
					mines += 1
				if board[i-1][j-1] == '*':
					mines += 1
				if board[i-1][j+1] == '*':
					mines += 1
				if board[i+1][j-1] == '*':
					mines += 1
				if board[i+1][j+1] == '*':
					mines += 1
				board[i][j] = str(mines)
	return board, proxy_board

def display_board(board):
	counter = 0
	for item in board:
		for tile in item:
			print(tile + '|', end = '')
			counter += 1
		print('')
	print('Expand the screen if the tiles look weird.')

def show_rules():
	print('You will be asked to choose the coordinate of the '
			'tile you wish to uncover.  First, choose how far '
			'down, starting from 0 as the uppermost row.  Then, '
			'choose how far to the right, starting from 0 as the '
			'leftmost column.')

def play_game(board, proxy_board, num_mines):
	display_board(proxy_board)
	tiles_swept = 0
	answer = input('Would you like to read the rules? Enter y for yes. ')
	if answer == 'y' or answer == 'Y':
		show_rules()
	while tiles_swept != len(board)*len(board[0]):
		down = ''
		right = ''
		while not down.isdigit():
			down = input('Choose the row of your tile: ')
		while not right.isdigit():
			right = input('Choose the column of your tile: ')
		down = int(down)
		right = int(right)
		while down >= len(board[0]) or right >= len(board):
			down = int(input('Out of bounds.  Choose the row again: '))
			right = int(input('Now choose the column again: '))
		if board[down][right] == '*':
			print('YOU LOSE!')
			display_board(board)
			return False
		else:
			proxy_board[down][right] = board[down][right]
			display_board(proxy_board)
	print('Congratulations!  You found all the mines.')
	return True

def main():
    # Get the dimensions of the board
    print('You can play on a board with the following dimensions.')
    print('1: 10x10')
    print('2: 25x25')
    print('3: 50x50')
    print('4: 100x100')
    choice = input('Choose 1, ' + '2, ' + '3, ' + 'or 4: ')
    while choice != '1' and choice != '2' and choice != '3' and choice != '4':
        choice = input('Choose 1, ' + '2, ' + '3, ' + 'or 4: ')
    if choice == '1':
    	height = 10
    	width = 10
    elif choice == '2':
    	height = 25
    	width = 25
    elif choice == '3':
    	height = 50
    	width = 50
    elif choice == '4':
    	height = 100
    	width = 100
    num_mines = ''
    while not num_mines.isdigit() or int(num_mines) >= width * height:
    	num_mines = \
    	input('Choose the number of mines.  It must be less than the number of tiles: ')
    num_mines = int(num_mines)
    if num_mines == 0:
    	print('You think I would let you play a game with zero mines?!!  HAHAHA game over')
    	return
    print('Generating game with', num_mines, 'mines.')

    board, proxy_board = make_board(width, height, num_mines)
    if not play_game(board, proxy_board, num_mines):
    	return

if __name__ == '__main__':
    main()
