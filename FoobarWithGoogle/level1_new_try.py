
from math import floor

panels = []

def square_breaker(area):
    
    n = floor(area**0.5)

    if n == 1:
        panels.append(1)

    while(area):

        perfect_square = floor(area**0.5)

        if perfect_square == 1:
            panels.append(perfect_square); break
            
        area -= perfect_square

            



def main():

    return


if __name__ == "__main__":
    main()


