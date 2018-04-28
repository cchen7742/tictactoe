EMPTY = ' '

def board_init(): 
	global board
	board = []
	for i in range(0,9):
		board.append(EMPTY)

def player_piece_init():
	global player1, player2
	player1 = input("Please select your piece X/O: ")
	if player1.upper() != "X" and player1.upper() != "O":
		print("Only Xs or Os please")
		player_piece_init()

	player1 = player1.upper()

	if player1 == 'O':
		player2 = 'X'
	else: 
		player2 = 'O'

def print_board(board):
	print("\n")
	for i in range(0,9):
		if i == 3 or i == 6:
			print("\n--------------")
		print(" {} |".format(board[i]), end = " ")

	print("\n")

def player_move(player):
	if board_full() or is_Win(player): 
		return
	try: 
		position = int(input('{}, Enter a position 1-9: '.format(player)))
		while not position in range(1,10) or board[position-1] != EMPTY:
			print("Invalid move")
			position = int(input('{}, Enter a position 1-9: '.format(player)))

		board[position-1] = player
		print_board(board)
	except ValueError:
		print("Invalid move")

def is_Win(player):
	#check rows 
	win_possibilities = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
	for a,b,c in win_possibilities:
		if board[a] == board[b] == board[c] == player: 
			print("Congrats {}, you have won".format(player))
			return True
	return False

def board_full(): 
	for i in range(0,9): 
		if board[i] == EMPTY:
			return False
	return True

def play_again():
	ans = input("Would you like to play again Y/N? ")
	if ans.upper() == "Y":
		return True
	return False

def main():
	global game 
	game = True
	print("Welcome to Tic Tac Toe\n")
	while game:
		board_init()
		print_board(board)
		player_piece_init()

		while not board_full():
			player_move(player1)
			if is_Win(player1):
				break
			player_move(player2)
			if is_Win(player2):
				break
		else: 
			print("It's a tie!")

		game = play_again()
	else: 
		print("\nThanks for playing \n")

main()

