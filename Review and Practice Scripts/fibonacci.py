#!python3
#fib() creates a fib_series list using the two iterators, a and b, to cycle in a loop until the correct values are reached.
#fib2() uses a series method, in a more formal way of writing it in math-language

def fib(n): #will return a list of fibonacci sequence with n # of elements
    blank = [] #inital blank list
    if n < 1:
        return blank #returns an empty list since an input of 0, means no elements
    blank.append(1)#now anything >0 will necessitate adding the first element to the fibonacci sequence
    if n < 2: 
        return blank #this returns the previously appended list, with one element
    blank.append(1)#now anything >1 will necessitate adding the second element, the second 1. list is now == [1,1]
    
    a,b = 1 , 1 #initialize the iterating variables for building the sequence beyond the first 2 elements
    for i in range(2,n):#for n == 2, we have an empty range here. So the previously built sequence is returned. 
        a, b = b, b+a   #for n >= 3, the loop will iterate the proper number of times to create 
        blank.append(b)
    return blank

def fib2(n): #will return a list of fibonacci sequence with n # of elements
    blank = []
    if n < 1:
        return blank
    blank.append(1)
    if n < 2:
        return blank
    blank.append(1)
    
    
    for i in range(2,n):
        blank.append(blank[i-1] + blank[i -2])
    return blank

test = 12

print ("\nFibonacci with cycle method is: ", fib(test))
print ("SUM = " , sum(fib(test)), end = "\n" *2)

print("Fibonacci with list appending method is: ",fib2(test))

print ("Length= " , len(fib2(test)))
