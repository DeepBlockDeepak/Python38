#1. Functions are Objects
'''
def add_five(num):
    print(num + 5)

print(
    (add_five), #<function add_five at 0x0000018FD9B84E50>
    type(add_five), #<class 'function'>
    sep = "\n"
)
'''

#2. Functions within functions
'''
def add_five(num):
    def add_two(num):
        return num + 2
    
    num_plus_two = add_two(num) #stores the +2 to 'num'

    print(num_plus_two + 3) #will take initial 'num' and add 5

add_five(10)
'''

#3. Returning functions fom functions
'''

def get_math_function(operation): # + or -

    def add(n1, n2): #addition op
        return n1 + n2
    
    def sub(n1, n2):  # subtraction op
        return n1 - n2

    #returning the above functions
    if operation == "+":   
        return add
    elif operation == "-":
        return sub

add_function = get_math_function('+')
print(add_function) #<function get_math_function.<locals>.add at 0x0000023974DF4EE0>
print(add_function(5,3)) #8

sub_function = get_math_function('-')
print(sub_function(5,3)) #2

'''

#4. Decorating a function
'''

def title_decorator(print_name_function):
    def wrapper():
        print("Mr. ", end = '')
        print_name_function()
    
    return wrapper

def print_my_name():
    print("Jordan")

decorated_function = title_decorator(print_my_name)

decorated_function()
print("\n***Using Decorators Below***\n")

#5. Decorators

@title_decorator    
def print_last_name():
    print("Medina")

print_last_name()   #obviates the need for line 64's idea

'''

#6. Decorators w/t Parameters
#as many parameters can be written in the internal function now

def title_decorator_wt_parameter(print_name_function):
    def wrapper(*args, **kwargs):   #passes the print() arguments into the wrapper() funciton
        print("Mr. ")
        print_name_function(*args, **kwargs)
    
    return wrapper

@title_decorator_wt_parameter
def print_a_name(name, age): #bc 'name' is passed, the wrapper needed the update
    print("{} is {} years old.".format(name, age))

print_a_name("Dingus", 90)




