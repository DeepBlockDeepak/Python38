
import random

def chess_position_dict():
    
    position_dict = {
     i : chr(ord('a') + i - 1) for i in range(1,9)
    }
    
    return position_dict



def drunk_knight(file, rank):

    file = list(chess_position_dict().values()).index(file) + 1 

    event_counter = 0   
    while rank in range(1,9) and file in range(1,9):

        rank += random.choice([-2,2,-1,1])
        file += random.choice([-1,1]) if rank in [-2,2] else random.choice([-2,2])

        event_counter += 1
    
    return event_counter




def knight_moves(trials, starting_file, starting_rank):

    number_of_valid_knight_moves = 0

    for i in range(trials):
        number_of_valid_knight_moves += drunk_knight(starting_file, starting_rank)

    return number_of_valid_knight_moves
    

#loops over every position on a chess board, and calculates the average number of moves it takes for a drunk knight to fall off
def simulations(trials = 10000):

    #'heat_map' will retain the total moves taken by the drunk knight at the starting positions, for 'trials' number of trials
    heat_map = {}
    position_dict = chess_position_dict()   #dictionary of the valid rank & file values in chess (8 each)

    #uses the position_dict to create a list of all 64 chess positions on the board
    chess_board = [file + str(rank) for file in position_dict.values() for rank in position_dict.keys()]

    for position in chess_board:
        heat_map[knight_moves(trials, position[0], int(position[1]))] = position 
    
    ranking_list = list(heat_map.keys())
    ranking_list.sort()

    
    print("\n\t\tTop positions and average number of moves:\n")

    for i in range(1, 11):
        greatest_val = ranking_list.pop()
        print(
            "--\t{}). {} with an average of {} moves per session.\t--".format(
                i, heat_map[greatest_val], round(greatest_val/trials,2)
                )
        )
    

simulations()
