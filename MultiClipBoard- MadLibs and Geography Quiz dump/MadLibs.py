#script will write a game of MadLibs into a directory's MadLibs.txt file
#User invents words which will replace 'adj, noun, verb' in a madlibs prompt
import os
import re
from time import sleep
#dir_name will be the location of madlibs.py, which contains the sub folders, mad_libs_scripts and MadLibsResults
dir_name = r'C:\Python38\Scripts\python38_practice\Chapter8\MadLibs'
script_dir = os.path.join(dir_name, "mad_libs_scripts")
result_dir = os.path.join(dir_name, "MadLibsResults")

def user_selection():    
    madlibs_menu= []    #initialize empty list, which will hold textfiles within script_dir
    for filename in os.listdir(script_dir):
        if os.path.isfile(os.path.join(script_dir,filename)):
            madlibs_menu.append(os.path.join(script_dir, filename))

    while True:

        print("\nEnter the full pathfile for the MADLIBS game you'd like to play.\n\
            \tYou may also choose from the menu.\n")
        sleep(1)
        print("Available MadLibs files:")
        sleep(1)
        for index, filename in enumerate(madlibs_menu):
            print (str(index + 1) + ".) " +os.path.basename(filename))
            sleep(1)

        user_file = input("\nType the menu number for the desired file, or paste your MadLib full filepath: ")
        try:
            if os.path.exists(user_file) and user_file.endswith(".txt"):#possibly exchange 'user_file' for 'os.path.abspath(user_file)'
                break
            
            #Handling the menu-selection case
            if type(int(user_file)) and int(user_file) > 0:
                
                user_file = madlibs_menu[int(user_file) -1] #user_file is now the madlibs text file path which will be used for RegEx
                break #exists the while loop
        except IndexError: #nonsense index assigned to user_file
            print ("\n{} is out of range. Try Again.\n".format(user_file),"\n"*2)
            sleep(1)
            continue #retry entire process
        except ValueError:
            print("\nPath doesn't exist or isn't a file. Try Again.\n")
            continue

    return user_file #user_file is the full path for the text file chosen by the user


def mad_libs():
    user_file = user_selection()    

    #user_file already exists, so open in read mode
    libs_file = open(user_file, 'r')
    libs_content = libs_file.read()
    libs_file.close()


    mlRegex = re.compile(r'(ADJECTIVE|NOUN|VERB|ADVERB)')
    mo = mlRegex.findall(libs_content)
    
    for word in mo:
        print()
        sub_word = input("Enter a(n): {}: ".format(word))

        libs_content = libs_content.replace(word,sub_word, 1)

    
    print ("\n", libs_content, "\n")
    return user_file, libs_content

def main_function_and_result_creator():
    user_file, libs_content = mad_libs()

    libsFileRegex = re.compile(r'\d+')#matches string that ends with at least one digit. Which is what we want for our .txt file names
    libs_mo =libsFileRegex.search(os.path.basename(user_file)) #may have to use str(os.path.basename(user_file))
    file_number = libs_mo.group()
    with open(os.path.join(result_dir, "madlibs" + file_number +"result.txt"),'w') as libsContentFile:
        libsContentFile.write(libs_content)
main_function_and_result_creator()