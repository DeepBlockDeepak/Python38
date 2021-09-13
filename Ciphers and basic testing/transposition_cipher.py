#!python3
from math import ceil, floor	#ceil() used because it obtains the number of rows needed for the transposition cipher


encrypt_key = 5 #... the encrytpion key

plain = "Sphinx of black quartz, judge my vow."  #plain-text, pre encrypted


#########################################################################
#																	  	#
# MY METHOD FOR ENCRYPTING "plain" WITH THE TRANSPOSITION CIPHER METHOD	#
#																		#
#########################################################################

def transposition_encrypt(encrypt_key, plain):
	
	cipher = ""	#will be used to store the encrypted plain-text

	for cols in range(encrypt_key):		#Loop over each column. The number of columns is determined by the encyrption key
		for rows in range(ceil(len(plain)/encrypt_key)):#the number of rows of the transposition cipher is related to the length of the plain-text divided by the encyrpt-key value rounded up
			if (rows*encrypt_key + cols) >= len(plain):		#This accounts for the "blank" cells of the transposition cipher... skip them
				continue
			cipher += plain[rows*encrypt_key + cols]			#access the appropriate char of the transposition cipher "grid"

	#print("\nCipher key = {}\n\"{}\" encrypts to:\n\"{}\"".format(encrypt_key, plain, cipher))
	return cipher

"""
#########################################################################
#	Trying to visualize the cipher-text as 'encrypt_key' number of 		#
# 	substring lists... The problem arises from the 'shaded boxes',		#
# 	resulting in chars getting assigned to the wrong substring list		#
#########################################################################

#BUG Fix this idea... Issues currently with the zip() ranges
iterator_list = list(range(encrypt_key))


#"chop" the cipher-text into as many columns as the cipher-key demands.
for (i,j) in zip(range(0,int(len(cipher)/2)), range(int(len(cipher)/2), len(cipher))):
	decipher += cipher[i] + cipher[j]
print("\n{} decrypts to \n{}".format(cipher, decipher))

#################################################
#	Other idea... similar to the above stuff	#
#	*Encode a 'row' idea, where you take into 	#
# 		account shaded rows 					#
#################################################
numOfColumns = ceil(len(cipher)/encrypt_key)
numOfRows = encrypt_key

cipher_list = [
	plain[i: i + numOfColumns] for i in range(0, len(plain), numOfColumns)
	]

#cipher_list is chopped, but doesn't take into account the "shaded boxes of the grid"

"""

############################################################################
#             My Attempt at Decrypting the Transposition Cipher            #
############################################################################
""" #BUG: FIX THE LOOP- NEEDS APPROPRIATE PLACEMENT OF THE 'row' AND 'col' VARIABLES
numOfColumns = ceil(len(cipher)/encrypt_key)
numOfRows = encrypt_key

for col in range(numOfColumns):	#(0, 8)
	for row in range(numOfRows):					#(0, 5)

		if (row + ceil(len(cipher)/encrypt_key)*col) >= len(cipher):
			print("should have skipped here at the value of {}".format())
			continue
		print("Row = {}  Col = {} ... Row+Col*height = {}".format(row, col, row + ceil(len(cipher)/encrypt_key)*col))
		decipher += cipher[row + ceil(len(cipher)/encrypt_key)*col]

print("\n\"{}\" decrypts to \n\"{}\"".format(cipher, decipher))
print("\n")
"""

############################################################################
#                       Cracking Codes Decryption Solution                 #
############################################################################

def transposition_decrypt(encrypt_key, cipher):

	decipher = "" #used to store the decrypted text from cipher, in the decrypting process
	
	column = 0
	row = 0
	#encrypt_key = 5

	plain = ['']*ceil(len(cipher)/encrypt_key)

	numOfRows = encrypt_key
	numOfColumns = ceil(len(cipher)/encrypt_key)


	for symbol in cipher:			#loop through each char in the cipher
		plain[column] += symbol		#assign the char to each sub-string member of 'plain', according to the 'column' index
		column += 1					#iterate the column index

		if (
			(column == numOfColumns) or		#'column' is not allowed to go out of range, so reset it to 0
			(column == numOfColumns - 1 and row >= numOfRows - (numOfRows * numOfColumns - len(cipher)))	#when the invalid, 'shaded boxes' are encountered
		):
			column = 0
			row +=1		#for an encryption-key/numOfRows value == 5, and string length == 37... only rows 0 & 1 are allowed (2,3,4 are 'shaded')

	decipher = "".join(plain)

	#print("\n\"{}\" decrypts to:\n\"{}\"".format(cipher, decipher))
	return decipher

cipher = transposition_encrypt(encrypt_key, plain)
decipher = transposition_decrypt(encrypt_key, cipher)


#print("\n\"{}\" decrypts  to \n\"{}\" when the encrypt_key of {} is used.".format(cipher, decipher, encrypt_key))
