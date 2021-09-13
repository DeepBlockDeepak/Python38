#function will guess the number in the user's head

def user_initializer():
    print ("Your mental number should lie between a low and high number.", end = "\n" * 3)
    
    while True: #loops until proper inputs are given to the test variables

        try:
            test_low = int(input("Pick a low number: "))
            test_high= int(input("Pick a high number: "))
            test_int = (test_high- test_low)/2
            #a range of numbers is now in play, with test_int as the middle value between 
            break #goes to testing loop in next function

        except ValueError: #except clause used if incorrect values are given by user, allowing repeat
            print ("Invalid input. Try again.", end = '\n'*3)
    return (test_low, test_high, test_int) #returns these variables for guesser() to use as input in the calculations


def guesser():
    test_low, test_high, test_int= user_initializer()

    while True:
        try:
            user_guess = input("Is your # higher('H'), lower ('L'), or equal ('E') to {0}?".format(round(test_int))) #user_guess will be used to re-assign the range of guessing in the loop

            if user_guess.upper() == "E" or not user_guess:
                print ("Cool, your # is {0}. Go home bitch.".format(test_int))
                break #game is over

            elif user_guess.upper() == "L":
                test_high = test_int #assingment allows new search space to be accessed in next loop
                test_int = round((test_high + test_low)/2)#middle value of new search space will be used
                
            elif user_guess.upper() == "H":
                test_low = test_int
                test_int= round((test_high + test_low)/2)

            else:
                print ("Wrong input.", end = '\n' *2)
                continue

        except AttributeError:
            print ("Wrong input.", end = '\n' *3)
            continue


guesser()

