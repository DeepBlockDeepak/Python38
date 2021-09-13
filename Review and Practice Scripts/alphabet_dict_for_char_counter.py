import pprint
while True:
    user_input = input("Enter an alphabetical string, pls friend.\n")

    #let chr() do the work for you to generate the alphabet
    alphabet_dict = {
        chr(ord('a') + i): 0 for i in range(26)
    }

    try:
        #if you're counting characters in a text string
        for letter in user_input:
            #ignore the space character, to allow for multiple words
            if letter.isspace(): 
                continue
            alphabet_dict[letter] += 1
        #successfully added all chars, let's get outta here
        break

    #generic error check, not sure what you may want to use here, or in addition
    except KeyError:
        print("no that non-alphabet character isn't acceptable here.")

pprint.pprint(alphabet_dict)


