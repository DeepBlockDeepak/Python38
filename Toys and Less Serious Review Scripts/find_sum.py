#find the 'sum' parameter among the elements in the list "array"

def find_sum(array, sum):

    array.sort()

    (low, high) = (0, len(array)-1)


    while low < high:

        if array[low] + array[high] > sum:
            high = high- 1

        elif array[low] + array[high] < sum:
            low = low + 1

        elif array[low] + array[high] == sum:
            print ("The numbers in the sorted array were found, {0} + {1}".format(array[low], array[high]))
            return
        else:
            print ("Sum was not found.")
            break

array = [
    5,
    7,
    9,
    2,
    4,
    101,
    22,
    1,
    5,
    3,
    3
]
sum = 106

find_sum(array, sum)

#from C:\\python38\\scripts\\python38_practice\\toys\\derp.py import derp
#derp()