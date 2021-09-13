#!python3 
#creating a lambda to do a list comprehensive version of a flattening algorithm

inner_0 = ['a', 'fortytwo', 'dogshit']
inner_1 = [1, 3, 4, 5]
inner_2 = [4,"four", "five", "siz", "six", 6]

outer_list = [
    inner_0,
    inner_1,
    inner_2,
    [100, 999]
]

#Goal is to flatten the 'outer_list' into a 1D array version of itself and its contents

#FIRST METHOD
flat_list = []

for item in outer_list:
    for sublist in item:
        flat_list.append(sublist)

print("First list using O(n^2)/double FOR loop method:\n",flat_list)

#SECOND METHOD- LIST COMPREHENSION
#The only previously declared variable which is needed is 'outer_list'
flat_list = [inner_item for second_list in outer_list for inner_item in second_list]
print("\nUsing list comprehension:\n", flat_list)

#THIRD METHOD- LAMBDA WITH LIST COMPREHENSION
#create a lambda function 'flatten()'
#creating variable names on the spot
flatten = lambda some_2d_list: [inner_element for two_dimensional_list in some_2d_list for inner_element in two_dimensional_list]

flat_list = flatten(outer_list)

print("\nUsing the Lambda:\n", flat_list)




