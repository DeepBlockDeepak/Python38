#!python3

import random, sys
from transposition_cipher import transposition_encrypt, transposition_decrypt

"""
#alternative method of importing methods in the transposition_cipher.py script
#chose not to use this because it's even uglier than what happens in C scripts, which are quite nice on this front actually

import transposition_cipher as tc
print(tc.transposition_encrypt(3, doggo))
"""

def main():

    #random.seed(42) #random seed, so that the same ciphers will be used each time... not sure why this is a good idea

    for i in range(20): #run 20 tests
        message = "ABCDEFGHIJKLMNOQRSTUVWXYZ" * random.randint(4, 40)   #take a random string of concatenated alphabets
        message = list(message) #turn the string into an iterable

        random.shuffle(message) #shuffle the list

        message = "".join(message)    #now message is a larger, scrambled, string version of its original self

        print("Test #{}: '{}...'\n".format(i + 1, message[:50]))    #only print 50 chars of the cipher


        #test each message with keys generated based on the len(message)/2
        for key in range(1, int(len(message)/2)):

            encrypted = transposition_encrypt(key, message) #pass the key and the message; returns a cipher string
            decrypted = transposition_decrypt(key, encrypted)   #pass the cipher to the decryption func; 
                                                                #...returns the decrypted message which should be identical to the original message passed to the encryption func()

            if message != decrypted:    #if the returned decrypted message doesn't match the initial input -> problem!
                print("Mismatch with key = {} and message {}".format(key, message))
                print("Decrypted as: " + decrypted)
                sys.exit()

    print("Transposition cipher test passed.")
    
if __name__ == "__main__":
    main()

