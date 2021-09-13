#recursive call to sum the entire file contents of a directory, including subfolders
#TODO: Figure out how to use the most accurate, non-recursive method for obtaining the size of an entire directory

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


path = 'C:\\Users\\rick_\\VirtualBox VMs\\Ubuntu'
print ("Recursive Method------------->", direc_size(path))

#testing against the following naive approach
total_size = 0
for filename in os.listdir(path):
    total_size += os.path.getsize(os.path.join(path,filename))
#print("="*20)

print ("Normal Approach   ----------->",total_size)

#print("="*20)

#TODO: Figure out how to use the most accurate, non-recursive method for obtaining the size of an entire directory
counter = 0
for folder_name, subfolders, filenames in os.walk(path):
    for file in filenames:
        counter += os.path.getsize((os.path.join(folder_name,file)))


print ("Walk Method ----------------->" , counter)
