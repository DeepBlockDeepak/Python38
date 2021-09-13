'''
A strong password is defined as one
that is at least eight characters long,
contains both uppercase and lowercase characters,
and has at least one digit.
You may need to test the string against multiple regex patterns to validate its strength.
'''
import re

def pw_detection(pw):
    if re.search(r'.{8,}'):
        return False
    elif re.search('[0-9]', pw) is None:
        return False
    elif re.search('[A-Z]',pw) is None: 
        return False
    elif re.search('[a-z]',pw) is None: 
        return False
    else:
        return True

if __name__ == '__main__':
    pw = input('Enter your password: ')
    if pw_detection(pw):
        print('Good, your password is strong!')
    else:
        print ('The password is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.')




def regex_strip(string, rm_str=None):
    if rm_str == None:
        return string.strip()
    else:
        string = string.strip()
        string_regex = re.compile(r'[rm_str]')
        return string_regex.sub('', string)


if __name__ == '__main__':
    string = input('Enter a string: ')
    rm_str = input('Enter the str you want to remove from the string or just clik enter: (Optional)')
    string = regex_strip(string, rm_str)
    print (string)




