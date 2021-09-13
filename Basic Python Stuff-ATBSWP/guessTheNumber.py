#script will run function which generates a random integer between 1-20 _
#(inclusive) and asks user to guess this value. Wrong answers are tallied_
#and when correct answer results, function ends with a print statement _
#displaying tally

import random

def guessNumber():
    computer_value = random.randint(1,20)
    
    
    guess_counter = 1

    user_name= input ('Hey. What is your name?  ')
    print ('\n')
    
    print ("Well, {0}, let's play a game, shall we?".format(user_name))
    

    while guess_counter <= 10:

        
        try:

            print ("\n")
            user_value = int(input("Guess my number, which is between 1 and 20 (inclusive): "))
            
            if user_value == computer_value:
                print ("You guessed correctly in {0} guesses!".format(guess_counter))
                break
            elif user_value < computer_value:
                print ('\n')
                print ('Sorry, that guess is too low')
                    
            elif user_value > computer_value:
                print ('\n')
                print ("Sorry, that guess is too high.")         

            guess_counter += 1
                
        except ValueError:
            
            print ('\n')
            print ('Guess must be an integer.')
            
            continue
    if guess_counter == 10:
        print ("You used up all {} of your guesses. You lose!".format(10))
guessNumber()
            
            
            
        
        
