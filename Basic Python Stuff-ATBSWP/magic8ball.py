import random


def getAnswer():
    

    while True:

        print ('\n')
        answerNumber = input('Enter a number between 1 and 9:')
        print ('\n')

        if not answerNumber.isnumeric():
            print ("This program requires an integer value. Please try again.")
            print ('\n')
            continue
        else:
                    
            if int(answerNumber) == 1:
                print ( 'It is certain')
            elif int(answerNumber) == 2:
                print ('eat balls')
            elif int(answerNumber) == 3:
                print ("you're so dumb")
            elif int(answerNumber) == 4:
                print ("i hate my life")
            elif int(answerNumber) == 5:
                print ( 'my life is suffering and nothing more')
            elif int(answerNumber) == 6:
                print ( "you're doing fine")
            elif int(answerNumber) == 7:
                print ( "Don't keep doing this to me")
            elif int(answerNumber) == 8:
                print ( "bob")
            elif int(answerNumber) == 9:
                print ( 'AHHHHHHHHH')
            elif int(answerNumber) == 11:
                print ("You're having a bad day, lemme tell ya.")
                continue

            

            else:
                
                userAnswer= input("something is off. Do you want to continue? (Y)")
                if userAnswer == 'Y' or userAnswer == 'Yes' or userAnswer == 'YES' or userAnswer == 'y':
                    continue #use 'break' here?
                else:
                    print (
                        "This is over with."
                        )
                    break
                

getAnswer()



