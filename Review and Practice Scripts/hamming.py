import numpy as np
import functools
import operator as op
import random
from math import ceil


# @BUG : Currently the display() function doesn't print arrays built with odd powers of 2 correctly (half squares)
#           Ex: 2^4 = 16, displays 16 bits fine. But 2^5 doesn't show 32 bits. But 2^6 will display the square properly
power = 6; how_many_bits = 2**power

#list of 16 random bits
bits = np.random.randint(0,2, how_many_bits)



def display(ex_list, n = power//2):
    for i in range(2**n):
        print(" ".join([str(chunk) for chunk in ex_list[(2**n)*i:(2**n)*i+(2**n)]]))
    #print("i = {}".format(i + 1))


#a pretty printing function
#display(lil_bits)

#from 3blue1brown's Hamming codes videos
def hamming_syndrome(bit_block):
    
    return(
        functools.reduce(
            lambda x,y: x ^ y, [i for i,bit in enumerate(bit_block) if bit]
        )
    )

#set the parity bits of the message 'bit_block'... After, it is then ready to be sent to receiver
def set_parity_bits(bit_block, i = 0):
    xor_sum = hamming_syndrome(bit_block)
    while(2**i <= xor_sum):
        bit_block[2**i] = not bit_block[2**i] if (xor_sum & 2**i) else bit_block[2**i]
        i += 1



#show the raw message; Find and print the hamming syndrome value; Set the parity bits of the message; 
#Display the message again, with the parity bits set properly. Message has been well-prepared at this point
#Incur an error by flipping a bit. Confirm algorithm by running the message back into the hamming syndrome(),
#and print the bit that was flipped.
display(bits)
print("--", hamming_syndrome(bits), "--")
print("<>" * 8, "\n")
set_parity_bits(bits)
display(bits)
print("--", hamming_syndrome(bits), "--")
bits[5] = not bits[5]
print("--After flipping the 5th indexed bit, hamming_syndrome == ", hamming_syndrome(bits), "---------")


'''
def display(ex_list, n = 16):
    for i in range(len(ex_list)//n):
        print(" ".join([str(chunk) for chunk in ex_list[n*i:n*i+n]]))

bits = np.random.randint(0,2,256)
'''

