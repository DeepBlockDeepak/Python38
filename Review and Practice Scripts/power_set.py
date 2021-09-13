"""
Problem: Given an integer k and a string s, find the length of the 
          substring that contains at most k distinct characters.
          For example, given s = "abcba" and k = 2, the longest substring with 
          k distinct characters is "bcb".
"""

#create a powerset of an input string
#filter that powerset's list-elements, so that you have a list of strings which have the appropriate amount of distinct characters AND are in the input string
#select the longest of these strings, return as the answer



def power_set(set):
  #length of a power set of some_set is equal to 2^(len(some_set))
  power_set_size = 2**len(set)
  #result will be the power set
  result = []

  for bit in range(0, power_set_size):
    #initialize a subset list, for each element in the power set
    sub_set = []
    
    #binary_digit will range from 0 to len(set)
    for binary_digit in range(len(set)):
      #bitmask to see if a bit is 'on' 
      if((bit & (1 << binary_digit)) > 0):
        #if it is on (not 0), append this to the powerset's element
        sub_set.append(set[binary_digit])
    #append element to the powerset 
    result.append(sub_set)
  return result

def filtering_solution_space(some_string, prune_number):
  #solution list will store all strings which are in "some_string" and_
  # which do not have more than 'prune_number' distinct characters
  solution_list = []
  
  #loop through each string-list element in the powerset
  for subset in power_set(some_string):
    
    #initialize empty dictionary to count distinct members within each element.
    dictionary_counter = {}
    #joined_string takes ex: ['a', 'b', 'a'] and spits out "aba"
    joined_string = "".join(subset)
    for character in joined_string:
      #ensure that each distinct character encountered will have a count of at least 1. 
      #multiple instances of the same character will increment by 1 as they are encountered
      dictionary_counter.setdefault(character, 0)
      dictionary_counter[character] += 1
    #figure out if joined_string is in 'some_string' has only 'prune_number' distinct characters
    if len(dictionary_counter.keys()) == prune_number and joined_string in some_string:
      solution_list.append(joined_string)
  
  #solution_list now contains strings which satisfy conditions
  #now we need to prune out the longest string within solution_list
  return solution_list

def pruning_solutions(some_string, prune_number):
  #answer_contains the answer, we must prune the longest answer
  answer_list = filtering_solution_space(some_string, prune_number)
  max_length = 0
  answer = ""
  for possible_solution in answer_list:
    #do a typical max_length pruner/thingy to find the longest string
    if len(possible_solution) > max_length:
      max_length = len(possible_solution)
      answer = possible_solution
  #bingo 
  return answer

input_a = "abcba"
prune_number_a = 2
input_b = "afbccbbffffca"
prune_number_b = 3
input_c = "cowwwwabunngaa!!"
prune_number_c = 5
input_strings = [input_a, input_b, input_c]
prune_numbers = [prune_number_a, prune_number_b, prune_number_c]

test_cases = [(x,y) for x, y in zip(input_strings, prune_numbers)]

for index, (input_string, prune_number) in enumerate(test_cases):
  print("Case {}".format(index + 1), pruning_solutions(input_string, prune_number))




"""
def power_sets(my_list):
  if len(my_list) == 0:
    return [[]]
  with_first = [ [my_list[0]] + rest for rest in power_sets(my_list[0:]) ]
  return with_first 
""" 

"""empty = []
print ('=================')
p_12 = power_set(empty)
print (p_12)
print ('=================')
p_13 = power_set(p_12)
print (p_13)
print ('=================')
p_14= power_set(p_13)
print (p_14)"""



#message = filter(lambda x: len(x.keys()) == prune_number and x in some_string, set_default_dictionary_keys)





"""
def power_sets(set):
  power_set_size = 2**len(set)
  result = []

  for bit in range(0, power_set_size):
    sub_set = []
    
    for i,binary_digit in enumerate(set):
      if((bit & (1 << i)) > 0):
        sub_set.append(binary_digit)
    result.append(sub_set)
  return result

dude = ['a', 'b', 'c']
for thing in power_sets(dude):
  print (thing)
 """
