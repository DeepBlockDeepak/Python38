# find_sum will look for the elements of an array which sum to the 'sum' parameter
def find_sum (array, sum):

    #initialize an empty dictionary, the hash map
    dict_map = {}
    #this empty list will be used to print off the solutions

    #loop through each i,e in array
    # check if (sum-item) is in array, and add to dict_map if it isn't. If it is, append to solution_list
    for index, item in enumerate(array):

        if (sum - item) in dict_map:
            print("Sum to {0} found at index {1} and {2} with values {3} and \
{4}.".format(sum,index, dict_map.get(sum-item), item, array[dict_map.get(sum-item)]))

        else:
            dict_map[item] = index

array = [3,7,12,11,0,9,8,1,8]
sum = 10

find_sum(array,sum)