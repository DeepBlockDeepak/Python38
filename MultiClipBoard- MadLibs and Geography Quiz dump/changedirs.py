#! python 3
# testing os module commands, in this case, creating new directories via python script

import os

'''
print (
    os.path.join('usr', 'bin', 'spam')
)
'''

'''
os.makedirs('C:\delicious\waffle\\nuts.docx')   #the \nuts.docx does not make a document file within the waffle directory.
'''

print (
    os.path.abspath('.'),
    end = "*"*8
)
