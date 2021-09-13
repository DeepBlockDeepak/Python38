from pprint import pprint
import random

board = []
for i in range(10):
    board.append(['0']*10)

def comp_place_ship(board):
    ships = {"A": 4, "B": 3, "C": 2, "S": 2, "D": 1}
    for key, value in ships.items():

        row = random.randint(0,len(board)-1-value) # fix the index error
        col = random.randint(0,len(board)-1)

        place = row+1,col+1#used for printing the coordinates(1 is added for converting indeces)
        print('The computer has placed ship {0} at {1}'.format(key, place))

        for k in range(value): # you alter a variable number of cells based on the length of the ship
            
            board[row+k][col] = key 
            

comp_place_ship(board)
pprint(board)
