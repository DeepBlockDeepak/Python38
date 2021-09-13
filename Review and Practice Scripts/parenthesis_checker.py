#!python3

def parenthesis_checker(sausage):
    stack = []
    parenthetical_pairs = {'(' : ')', '{' : '}', '[' : ']'}

    for char in sausage:
        
        #if the char is a left parenthesis, add it to top of stack
        if char in parenthetical_pairs.keys():
            stack.append(char)

        #if the char is a right parenthesis, check it
        if char in parenthetical_pairs.values():
            if not stack:   #when there are more right parentheses than left
                print("Invalid sausage")
                return
            #should both pop off the stack, and check symmetry too
            if parenthetical_pairs[stack.pop()] != char:
                print("Invalid stuff")
                return
                
    #only good stuff hits this print statement
    print('good , thanks')


invalid_polish_sausage = "(e) = m*c ^ {2]"
good_vienna_sausage = "(e) = {m*c} ^ {2}"
parenthesis_checker(invalid_polish_sausage)
parenthesis_checker(good_vienna_sausage)





