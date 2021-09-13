#from practice projects on pg 102
#use a while loop and a for loop to solve

spam = [
    "apples",
    "bananas",
    "tofu",
    "cats"
    ]

dingus =[
    1,
    "so",
    "what",
    3,
    5.666
    ]

#using for loop
def comma(input_list):
    empty_string = ""
    for index in range(len(input_list)):
        if index < len(input_list)-1:
            empty_string += str(input_list[index]) + ", "
        else:
            empty_string += "and " + str(input_list[index])

    return empty_string

print (comma(spam))
print(comma(dingus))

print ('\n' *1)


def while_comma(input_string):
    empty_string = ''
    counter = 0
    while counter < len(input_string)-1:
        empty_string += str(input_string[counter]) + ', '
        counter += 1
    empty_string += "and " + str(input_string[len(input_string)-1])
    return empty_string

print (while_comma(spam))
print (while_comma(dingus))
