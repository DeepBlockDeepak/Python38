#!python3

import re

testRegEx = re.compile(r'''(
    (```py)
    ((.*\n?)*)
    (```)

)''', re.VERBOSE)

teststuff = "this is a pile of rubbish but ```py heresthegoodstuff \n more good stuff \n and me too ``` "

match_object = testRegEx.findall(teststuff)
print(match_object[0][2])


