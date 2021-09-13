'''
def collatz(number):

    if number == 1:
        return

    else:

        
        if number % 2 == 0 :
            print (number // 2)
            return collatz(number // 2)
        else:
            print (number * 3 + 1)
            return collatz(number * 3 + 1)
'''
def collatz(number):

    while number != 1:
        if number % 2 == 0:
            number = int(number / 2)
            print (number)
        else:
            number = 3*number + 1
            print (number)
    return number



def run_collatz():
    while True:
        
        try:
            starter = int(input("Enter an integer to start its Collatz sequence: "))

            collatz(starter)

            break
            
        except ValueError:
            print ("You must enter an integer value. Try again.")
            continue
run_collatz()