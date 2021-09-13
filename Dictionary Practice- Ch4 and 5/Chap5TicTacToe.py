from pprint import pprint




board= {
	"top-L": " ",
	"top-M": " ",
	"top-R": " ",
	"mid-L": " ",
	"mid-M": " ",
	"mid-R": " ",
	"low-L": " ",
	"low-M": " ",
	"low-R": " "
	}
def print_board(board):
    print(board["top-L"] + '|' + board["top-M"] + '|' + board["top-R"])
    print ('-+-+-')
    print(board["mid-L"] + '|' + board["mid-M"] + '|' + board["mid-R"])
    print ('-+-+-')
    print(board["low-L"] + '|' + board["low-M"] + '|' + board["low-R"])


print ("The available spaces are: \n")

for key in board.keys():
    print (key)



for i in range(9):
    print ("\n")
    print_board(board)
    print ("\n")

    while True:
        move = str(input("What is your piece?"))
        turn = str(input("Pick a space:"))
        try:
            if board[turn] != " ":
                print ("This spot is taken. Try again. \n")
                continue
            else:
                board[turn] = move
                break
        except KeyError:
            print("That space doesn't exist. Try again. \n")
            continue
print_board(board)


                
                
                
            
            


