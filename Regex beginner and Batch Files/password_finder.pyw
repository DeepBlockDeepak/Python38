#! python3
#function will read text from user's clipboard
#and return the matched passwords to an existing password_storage.txt file for storage
import re
import pyperclip

def find_password():
    #create the Regular Expression object, passwordRegEx, 
    #passwordRegEx will process a pattern for finding passwords in string of some database's passwords
    passwordRegEx = re.compile(r"""(

        (pwd|password)     #looks for leading 'password', case insensitive do to IGNORECASE
        (:|-)?              #optional ':' or '-'
        (\s)?            #optional space after
        (.*)                #anything and everything that follows, This is what we're after

    )""", re.VERBOSE| re.IGNORECASE)

    #take the database info as string from the user's clipboard, store in 'user_input'
    user_input = str(pyperclip.paste())

    matches = []
    #'groups' is a tuple of all the matched groups in the passwordRegEx
    #we only want groups[4], where the password is stored
    for groups in passwordRegEx.findall(user_input):
        matches.append(groups[4])

    #if there were matched passwords, write to the existing storage .txt file
    if len(matches) > 0:
        #assuming 'password_storage.txt' already exists in the cwd of this script.
        with open('password_storage.txt', 'a') as storage_file:
            storage_file.write("-_--_--_--_--_--_--_--_--_--_--_--_-\n")
            storage_file.write('\n'.join(matches))
            storage_file.write("\n-_--_--_--_--_--_--_--_--_--_--_--_-")
    else:
        print("No passwords found.")
find_password()
