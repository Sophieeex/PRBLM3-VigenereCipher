# Name: Sophia Marie T. Reyes
# Year & Section: BSCpE 1-5
# Laboratory Program: Problem 3 - The Vigenere Cipher

# create a function that provides a value for each character 
# from the inputted text to generate an encrypted message

def encryption(message, key):
    encrypt_text = []
    for i in range(len(message)):
        value = (ord(message[i]) + ord(key[i])) % 26
        value += ord("A")
        encrypt_text.append(chr(value))
    return ("".join(encrypt_text))


# formats the key based on the length of the inputted text

# the user type the message and key
# the output printed is based on the condition met
