#! python3
#phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard and writes them into a .txt file. Directory choice is up to the user
#re module for regEx, pyperclip for user's clipboard as input, os for opening and closing files into directories
"""
This page can be CTRL+A and copied for input: https://www.mapleton.us/Domain/1079 . Output will print as well as paste to user clipboard
"""
import re, pyperclip , os


#the dirname of the .txt file will be 'directory'
directory = "C:\\Users\\Jordan\Documents\\Contact Info"


#pattern_matching() function processes the desired phone number and email address patterns, and outputs RegEx objects
def pattern_matching():
    phoneRegex = re.compile(r'''(
        (\d(-|\.))?             #this is for numbers that begin with 1-800 OR 1.800, optional
        (\d{3}|\(\d{3}\)(-)?)?  #area code, optional
        (\s|-|\.)?              #separator after area code, optional
        (\d{3})                 #middle three digits after area code 
        (\s|-|\.)?              #separator, optional
        (\d{4}|\w{4})           #last four digits ; \w character as an option for numbers with words at the end. ex: 1-800-444-TALK
        ((,)?\s*(ext|x|ext\.|Ext|Ext\.|Extension|extension)\s(\d{1,3}))?  #for many different possible extension formats, optional


    )''', re.VERBOSE)       #VERBOSE allows for multi-line raw string, and it ignores whitespaces between the groups


    #emailRegex simply pattern matches most email addresses, using the same Verbose method
    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+         #opening username, must be at least one character- customized match object for all text, (upper and lower), any digit and the allowed username symbols
        @                         # must use an @ symbol
        [a-zA-Z0-9.-]+            #domain name, can be at least one character
        \.[a-zA-Z]{2,4}           #top-level domain
    )''', re.VERBOSE)               

    return phoneRegex, emailRegex #returning two regular expression objects



#now that the regular expressions have been specified, the pasting and copying functions follow


def processing_matches():
    #import the regular expressions from pattern_matching()
    phoneRegex, emailRegex = pattern_matching()
    
    #'text' stores the user-copied material from their clipboard
    text = str(pyperclip.paste())
    
    #assign a blank list to matches. matches will contain the final data we're looking for 
    matches = []

    #for each group of tuples within the phoneRegex.findall() list, pluck out the main numbers and append to 'matches'.
    for groups in phoneRegex.findall(text):

        #groups[3], groups[5], and groups[7] contain the digits, 'phoneNumber is a string of the standard format we want our phone numbers to look like
        phoneNumber = '-'.join([groups[3], groups[6], groups[8]])
        #in the case that a phone number is a 1-800 or 1.800 number
        #the '1-' or '1.' item must be added, however the '-' or '.' respectively must be excised in order to result in the correct standard format 
        if groups[1] == '1-' or groups[1] == '1.':
            phoneNumber = '-'.join([groups[1][0], groups[3], groups[6], groups[8]])

        #if the phone number does not have an area code, ex: 555-5555 ext 444 | 777-7777, then phoneNumber must be overwritten to allow the correct group selection
        if groups[3] == '':
            phoneNumber = '-'.join([groups[6], groups[8]])
        
        #If the phone number does have an extension, add it to the phoneNumber string
        #the extension digits are the last item in the tuples
        if groups[len(groups)-1] != '':
            phoneNumber += ' x ' + groups[len(groups)-1]
        
            
        matches.append(phoneNumber)

    
    for groups in emailRegex.findall(text):
        #emails are nice enough, because there is only a single group in the regex; no need to use list indexes
        matches.append(groups)
    
    return matches #returns a list of numbers which are written in a standard format (ex: 715-000-2345)


#the pypcerlip.copy() method takes in a single string value, not a list of strings. 'matches' needs to be .join()'d to make this happen
#global variable 'directory' used for writing the standard format output of the pattern matching process to a .txt file. 
#the .txt file is named by the user 
def writing_to_file():
    matches = processing_matches()
    #use the newline, \n, to join each Match Object within 'matches'
    if len(matches) > 0:
        presentation = '\n'.join(matches)
        #'matches' is now on the user clipboard

        print ("\n" *2)

        
        filename= input("What would you like to name this contact list?:\n\t")

        filename+=".txt"

        absolute_path = os.path.join(directory, filename)
        
        '''
        filenameObject = open(absolute_path, 'w')
        filenameObject.write(presentation)
        filenameObject.close()
        '''
        #following is used to do what the above commented code does
        with open(absolute_path, 'w') as filenameObject:
            filenameObject.write(presentation)
        
        print ("\n{0} was copied into the directory: \n\n {1}\n".format(filename, directory))

        
        #this commented code can be used if having the output printed to the terminal and copied to the clipboard is desired
        '''
        pyperclip.copy(presentation)
        print (presentation)
        '''
    #if there are no matches found in the clipboard, the len(matches) == 0
    else:
        print("No matches were found.")

writing_to_file()