
import os
#dir_name is string of a file path
def direc_size(dir_name):
    #check if dir_name is a file. if so, return the size of the file
    if os.path.isfile(dir_name):
        return os.path.getsize(dir_name)
    
    #else, dir_name is a directory
    else:
        #loop over the list of items in the directory, and return the function call on the item
        total = 0
        for base_name in os.listdir(dir_name):
            total += direc_size(
                os.path.join(
                    dir_name, base_name
                )
            )
        return total
