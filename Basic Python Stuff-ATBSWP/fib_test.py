def fibonacci(n):
    if n <1:
        print ("Invalid input.")
    
    elif n < 2:
        print (1)
    else:
        a,b= 0,1
        for place in range(n):
            a , b = b , b+a
            print (a)


fibonacci(-20)
print("************")
fibonacci(0)
print("************")
fibonacci(1)
print("************")
fibonacci(2)
print("************")
fibonacci(11)
print("************<<<<<<<>>>>>>>>")

def fib_recursion(n):
    if n <= 0:
        print(1)
    else:
        print (n)
        return fib_recursion(n-1) + fib_recursion(n-2)
print (fib_recursion(20))

