#First Python project


player1 = None
player2 = None


def player_piece_init():
	player1 = input("Please select your piece X/O: ")
	if player1.upper() == 'O':
		player2 = 'X'
		player1 = 'O'
	else: 
		player2 = 'O'
		player1 = 'X'



def print_board(board):

