def back(name):
    blank = ''
    i = len(name)-1
    while i >= 0:
        blank += name[i]
        i -= 1
    print (blank)
    
    return blank


def backs(name):
    blank = ''
    curse = len(name)-1
    for i in range(len(name)):
        blank += name[curse]
        curse -= 1
    print (blank)
    return blank

name = 'Johnny'
'''
back(name)
print ('\n' *3, '*********')
backs(name)
'''

#mario() will print a tower with a base of 'height' and a height of 'height' 
#the layers will be centered around an empty space, comprised of asterisks
def mario():
    height = int(input("What size tower?"))
    
    #center = height-1
    print ("*".center(2*(height), " "), end = "")
    for i in range(height):
        """following print statement works only when the (center -= 1) line is uncomented, AND the second print statement is commented out"""
        #print (" "*center + "*"*i + " " + "*" *i)
        
        print (("*"*i).rjust(height-1, " ") + " " + ("*"*i).ljust(height-1))

        """Uncomment here if using the first print statement method of tower creation"""
        #center -= 1
mario()