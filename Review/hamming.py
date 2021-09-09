import numpy as np
import functools
import operator as op
import random
from math import ceil

random.seed(2)

power = 4; how_many_bits = 2**power

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

#set the parity bits of the message, bit_block then ready to be sent out
def set_parity_bits(bit_block, i = 0):
    xor_sum = hamming_syndrome(bit_block)
    while(2**i <= xor_sum):
        bit_block[2**i] = not bit_block[2**i] if (xor_sum & 2**i) else bit_block[2**i]
        i += 1


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

