#code demonstrates efficacy of regular expressions

########## the findall() method returns a list....... the search() method returns a MatchObject which requires the group() method############

'''
def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False 
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False 
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

foundNumber = False
for i in range(len(message)):
    chunk = message[i:i + 12]
    if is_phone_number(chunk):
        print ("Phone Number found : " + chunk)
        foundNumber = True
if not foundNumber:
    print ("No phone number was found.")
'''
"================================================="
import re

#findall is used to select every pattern matching object in 'message'
message = 'Call me 514-444-3434 tomorrow, or at 415-678-9845.'

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo =phoneNumRegex.findall(message)

#mo is a list 
print ([number for number in mo])

print ("=========================================")

#uses the group() method. The pattern passed to compile() specifies a difference between the area code and the rest of the phone number
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search("My number is 415-555-4242.")

print (mo.group(2)) # == 555-4242
#groups() method returns all groups at once
areaCode, mainNumber = mo.groups()
print ("Area code is {0}; main number is {1}".format(areaCode, mainNumber))

print ("=========================================")


#uses escape character on parantheses in the case where the pattern object has parentheses

phoneNumRegex= re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo = phoneNumRegex.findall("My phone number is (415) 555-4242 and hers is (333) 444-5555.")
#areaCode, mainNumber = mo.group(1), mo.group(2) # == '(415)', '555-4242'

#print ("Area code is {0} and main number is {1}".format(areaCode, mainNumber))

for number in mo:
    print (number[0], number[1])

print ("=========================================")


#using the pipe character with findall() 
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.findall('Batman and Tina Fey were on set today but Tina Fey and Batman didn\'t give a fuck.')
"""
for hero in mo1:
    print (hero)
"""