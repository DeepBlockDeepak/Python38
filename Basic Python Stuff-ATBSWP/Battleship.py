from random import randint
import random
for dog in cat:


board = []

while True:
	try:
		board_size = int(input("How big would you like the board length to be?: "))

		for i in range(board_size):#loops over length of board_size
			board.append(["O"] * board_size) #makes int(board_size) rows
		break

	except ValueError:#Exception handling for bad input to the global variable board_size
	    print ("You must type an integer.")
		print("\n"*2)
		continue

#print_board function displays the full contents of the list of lists within the global variable board.
def print_board(board_in):
  for row in board_in: #for each list of [O,O,O,O,O]
	print ("    ".join(row)) #takes items in a list, and concatenates them with a filler in between the items
	print("\n"*2)
print_board(board)

#The following variables will establish the location of the computer opponent's Battleship
#Because the board is a square, ship_row and ship_col will use the len(board) argument for randint()
#if the game is recoded to allow the user to choose how many rows *AND* columns the board has, then this will not do_
#because len(board) == the number of rows; the number of columns would then be len(board[0]), for instance.)

ship_row = randint(0, board_size-1)
ship_col = randint(0, board_size-1)#-1 is used so that the index == len(board) isn't used later on

#the following "second" functions are used to establish a second ship ("Destroyer") on the board, for a second round of the game
#once the first Battleship is sunk or escapes, the script will perform the same gameplay for the second ship
#The following code needs to place a second ship on the board which does not have the same location as the first ship
destroyer_row= random.choice([i for i in range(board_size) if i != ship_row])
destroyer_col = random.choice([i for i in range(board_size) if i != ship_col])


for turn in range(board_size):
  print (("Turn") , turn + 1)
  guess_row = int(input("Guess Battleship Row: "))-1
  guess_col = int(input("Guess Battleship Col: "))-1
  print("\n"*2)

  if guess_row == ship_row and guess_col == ship_col:
	print ("Congratulations! You sank my Battleship!\n")
	board[guess_row][guess_col] = "H"
	print_board(board)
	print("\n"*2)
	break

  else:
	if guess_row not in range(len(board)) \
	or guess_col not in range(len(board)):
	  print ("Oops, that's not even in the ocean.\n")

	elif board[guess_row][guess_col]== "X":
	  print ("You guessed that one already.")

	else:
	  print ("You missed my Battleship!\n")
	  board[guess_row][guess_col]="X"

	if turn == board_size -1:
	  print ("You lose, loser! Game Over")

	print_board(board)

print ("A Destroyer appears on the scene.")
print ("\n"*3)

board.clear()

for i in range(board_size):
    board.append(["O"] * board_size) #makes int(board_size) rows

print_board(board)

for turn in range(board_size):
  print (("Turn"), (turn + 1))
  guess_row_second = int(input("Guess Destroyer Row: "))-1
  guess_col_second = int(input("Guess Destroyer Col: "))-1

  if guess_row_second == destroyer_row and guess_col_second == destroyer_col:
	print ("Congratulations! You sank my Destroyer!")
	break

  else:
	if guess_row_second not in range(len(board)) \
	or guess_col_second not in range(len(board)):
	  print ("Oops, that's not even in the ocean.")

	elif board[guess_row_second][guess_col_second]== "X":
	  print ("You guessed that one already.")

	else:
	  print ("You missed my Destroyer!")
	  board[guess_row_second][guess_col_second]="X"

	if turn == board_size-1:
	  print ("You lose, loser! Game Over")

	print_board(board)