#! python 3
#need os module for the walk() method
import os

def walk_max_size(folder):
    #counter for the max filename length
    max_size = 0
    #dictionary for holding the path key and its length value
    file_dict = {}

    #walk the directory, and track the absolute filepath string length 
    for folderName, subfolders, filenames in os.walk(folder):

        for subfolder in subfolders:

            filename_size = len(os.path.join(folderName, subfolder))

            if filename_size > max_size:
                
                max_size = filename_size
                #dictionary => {absolute file path: string length}
                file_dict[subfolder] = filename_size

        for filename in filenames:
            #join() merges the directory path to the basename 
            filename_size = len(os.path.join(folderName, filename))

            if filename_size > max_size:

                max_size = filename_size
                #dictionary => {absolute file path: string length}
                file_dict[os.path.join(folderName, filename)] = filename_size
    
    #invert the key:value pairs to access the correct filepath based on known max_size "key"
    inv_file_dict = {v:k for k,v in file_dict.items()}
    print (
        os.path.abspath(inv_file_dict[max_size]),
        " = the largest path length in the directory = ",
        max_size,
        " characters long."
        )
        
walk_max_size(r'C:\Program Files')	
