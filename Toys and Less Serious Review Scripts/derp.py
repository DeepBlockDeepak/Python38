#!python3
#derp.py will take in user text as input, and return derp format. IN-> "shut up" Out-> "ShUT uP"
import pyperclip #allows script to store output into clipboard
from random import * # random module used for capitalization of string characters


def derp():
    while True:
        user_input= input("Enter string to derp: ") #user_input obtains the string to derpify
        empty = "" #empty string allowing output to append
        for i in range(len(user_input)): #cycle through each index of user's input 
            rand_flip = randint(0,1) #generate either a 1 or a 0 and store in rand_flip
            if rand_flip == 1:
                empty += user_input[i].upper()
            else: 
                empty += user_input[i].lower()
        empty += "!!!!"
        pyperclip.copy(empty) #copies to clipboard
derp()
