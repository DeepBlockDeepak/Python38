#solution() should search within range(0,s) for which s is in range(1,1000001) for largest value
# n for which n^2 < s. Then, appending to a list, find the remaining squares until the sum of the squares matches 'area'
def square_factor_seeker(area):
    possible_sqrts = []
    panel = []
    '''
    loop through values that go up to and include the sqrt(area), because sqrt(area) is 
    the biggest number that is allowable in the solution list
    '''
    for i in range(1,int(area**0.5) +1):
        possible_sqrts.append(i**2)
    '''
    at this point, possible_sqrts is now a list of 
    squared values. Working backwards, through this list,
    panel must .append() values up until the sums match area
    '''
    
    counter = len(possible_sqrts)-1 
    while counter >=0:
        #possible if statement to immediately break if (area - possible_sqrts[counter] < 0)
        if area - possible_sqrts[counter]>= 0: #if the total panel area still has room after subtracting away the largest sqrt panel
            panel.append(int(possible_sqrts[counter]**0.5)) #add this sqrt panel size to the solution list
            area -= possible_sqrts[counter] #decrement area by the added panel size
        else:
            counter -= 1 #next
    '''
    now that area has shrunk, it may not be == 0.
    Because it is a minimum, we should have only the "1"
    squares leftover. 
    '''
    for i in range(area):
        panel.append(1)

    return panel

#print (test_val, " = ", square_factor_seeker(test_val), "****", sum(square_factor_seeker(test_val)))
test_val1 = 100369766
test_val2 = 17
test_val3 = 18
for test_input in range(789, 18235):
  print(str(test_input) + " = " + '^2 + '.join(map(str, square_factor_seeker(test_input))) + "^2")

#print("{} + ".format(i)) for i in square_factor_seeker(test_val) if i < len(square_factor_seeker(test_val)) - 1 else print(i)
