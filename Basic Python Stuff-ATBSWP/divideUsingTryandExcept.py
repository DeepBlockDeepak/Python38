def divideby(thingy):
    try:
        return 42/ thingy
    except ZeroDivisionError:
        print (
            "Hey, fucker, you can't do that at a value of: {0}".format(thingy)
            )
    

r = [1,2,3,4,0,5]
new_list = [divideby(item) for item in r]
print (new_list)






        
