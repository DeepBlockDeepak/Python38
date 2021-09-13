#! python3

#mcb.pyw allows user to save their clipboard contents into a keyword. This can be done multiple times with different keywords
#script called from terminal via PATH variable and .bat file
#if sys.argv[1] == 'list', then the script will print a list of the available keyword 'clipboards' in store
#if sys.argv[1]== 'save' then the clipboard contents will be pasted into the keyword at sys.argv[2]
#if sys.argv[1] == 'del' or 'delete' then the keyword and it's contents will be deleted from the mcb
#if sys.argv[1] is in the shelve object, then this keyword's corresponding contents will be copied to the clipboard

import shelve
import sys
import pyperclip
import os

#option here to change the directory where the shelve files will be stored
directory = r'C:\\Python38\\Scripts\\python38_practice\\MultiClipBoard- MadLibs and Geography Quiz dump'

#opens the Shelve File and closes the Shelve File
with shelve.open(os.path.join(directory, 'mcb')) as shelfFile:

    
    #condition assesses a command to store clipboard text into a keyword (keyword located at sys.argv[2])
    if len(sys.argv)== 3 and sys.argv[1].lower() == "save":
        shelfFile[sys.argv[2]] = pyperclip.paste() #Shelve objects are similar to dictionaries, so this assignment works.

    #this condition should allow a user to delete a previously stored keyword, and it's value within the shelfFile, followed by copying the remaining keywords available
    elif len(sys.argv) == 3 and sys.argv[1].lower() in ["del","delete"]:
        
        del shelfFile[sys.argv[2]]
        
        pyperclip.copy("Multiclipboard keys:\n" + str(list(shelfFile.keys())))
    
    #concerning cases where the user is trying to list all saved keys, or trying to call the value of a saved key
    elif len(sys.argv) == 2: 

        if sys.argv[1].lower() == 'list': #example " mcb list " will return the following string of the of the shelfFile keys
            pyperclip.copy("Multiclipboard keys:\n"+ str(list(shelfFile.keys())))
        
        if sys.argv[1].lower() in shelfFile: #example "mcb dog " will return the clipboard content value of the key 'dog' if dog is in shelfFile

            pyperclip.copy(shelfFile[sys.argv[1]])
