# substitution cipher encryption program

import random
import string

# let's define our constants using some string defaults
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars) # we can now parse the chars string into a list
key = chars.copy()  # since we're gonna need a key, let's create an identical list

# we're going to shuffle the key list every time the program starts
random.shuffle(key)

# Encryption
plain_text = input("Enter your text: ") # we first take the user input
cipher_text = ""                        # and declare the ciphered text

# then, we can iterate over every letter in the input text
for letter in plain_text:
    # for each letter, we're gonna get the corresponding index of in the chars list
    index = chars.index(letter)
    # and we'll append the corresponding key in the indexed position to the encripted text
    cipher_text += key[index]

print(f"Your cipher text is: {cipher_text}")

# Decryption
cipher_text = input("Enter your text: ")
plain_text = ""

# to decrypt the message, we can just swap key and chars
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Your plain text is: {plain_text}")