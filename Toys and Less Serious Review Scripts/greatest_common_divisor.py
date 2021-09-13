import time


def gcd_input():#Function obtains two integers from user, to be used in the logic
    time.sleep(.5)
    print("Let's find the greatest common divisor between two numbers.")
    time.sleep(.5)
    first_number = int(input("Select the first number: "))
    time.sleep(.5)
    print("beep boop beep boop")
    time.sleep(.5)
    second_number = int(input("Select the second number: "))
    time.sleep(.5)
    print ("beeeeep booooop done!")
    
    return first_number, second_number


def gcd():
    a, b = gcd_input()

    if a < b :
        smaller = a
    else:
        smaller = b
    gcd = "No gcd found"
    for i in range(2, smaller + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    print(gcd)

def find_gcd(x,y):
    while (y):
        print("---------")
        print("x = {} y = {}".format(x,y))
        x,y = y, x%y
        print("x = {} y = {}".format(x,y))
    print("ANSWER = {}".format(x))

find_gcd(804, 10122)
'''
        if a%b == 0:#if and elif statements check if the user inputs are divisible by one another
            print (b)
        elif b%a == 0:
            print(a)

        else:
            empty = []
            for i,j in zip(range(2,a), range(2,b)):
                if a%i == 0 and b%i == 0:
                    empty.append(i)
                if a%j == 0 and b%j == 0:
                    empty.append(j)
'''
