#! python3

#ord(char) converts ascii to numerical value
#chr(int) converts integer to ascii character

#pyperclip used for the message grabbing
import pyperclip

def user_menu():

    #try:

    user_selection = input(
        "Would you like to encrypt or decipher? (e or d)?\n"
    )

    if user_selection.lower() in ["e", "encrypt"]:
        caesar_encrypt()
    
    elif user_selection.lower() in ["d", "decipher"]:
        caesar_decipher()

    else:
        print("You gave a funny input")

"""
    except TypeError:
        print("Cannot accept that input")
"""

def caesar_encrypt():

    #comment out the following and uncomment the 'with open()' to grab plain text from a file in OS
    user_plaintext = pyperclip.paste()
    """
    with open(r'C:\Python38\Scripts\python38_practice\Ciphers\some_test.txt', 'r') as text:
        user_plaintext = text.read()
    """
    #user_plaintext = 
    cipher_text = ""

    cipher_key = int(input("What is the cipher key value? "))

    for item in user_plaintext:

        if item.isalnum():

            if item.isupper():
                cipher_text += chr(
                    (ord(item) + cipher_key - ord('A')) % 26 + ord('A')
                )
            else:
                cipher_text += chr((ord(item) + cipher_key - ord('a')) % 26 + ord('a'))

        else:
            cipher_text += item

    print("Message encrypted.... Cipher-text copied")
    pyperclip.copy(cipher_text)


def caesar_decipher():

    user_ciphertext = pyperclip.paste()
    plain_text = ""

    cipher_key = int(input("What is the cipher key value? "))
    
    for item in user_ciphertext:
        if item.isalnum():

            if item.isupper():
                plain_text += chr(
                    (ord(item) - cipher_key - ord('A'))  % 26 + ord('A')
                )
            
            else:
                plain_text += chr(
                    (ord(item) - cipher_key - ord('a'))  % 26 + ord('a')
                )
        else:
            plain_text += item
            
    print("Cipher-text decrypted.... Plain-text copied")
    pyperclip.copy(plain_text)

user_menu()