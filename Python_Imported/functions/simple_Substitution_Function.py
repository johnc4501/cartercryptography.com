#Simple Substitution Cipher

""" Create your substitution key by 
reorganizing the alpahabet, making sure not to repeat any letters. 
The position of a letter in the new alphabet corresponds with the 
same letter position on the original alphabet, 
for example if your ordered the first three letters in your substituion key as VRI, 
your plaintext A would encrypt to V, 
B would encrypt to R, and C would encrypt to I.
"""

#define our variables
true_Alphabet = 'abcdefghijklmnopqrstuvwxyz'
user_Selection = input("Input E for encryption or D for decryption (WARNING - CASE SENSITIVE):")
user_Input = input("Enter plaintext for E, or ciphertext for D:")
new_Alphabet_Key = input("Enter a reordered alphabet to use as your substitution key:")

#Define our Encryptiion and Decryption Functions
def SS_Encryption(user_Input, new_Alphabet_Key, true_Alphabet):
	#Create an encryption dictionary
	key_Encryption_Dictionary = dict(zip(true_Alphabet, new_Alphabet_Key)) #use zip to allow more than one string (arguments) to be paired together as one argument
	return ''.join(key_Encryption_Dictionary.get(letter.lower(), letter) for letter in user_Input) #use .join to join all items from the dictionary into a string

def SS_Decryption(ciphertext, new_Alphabet_Key, true_Alphabet):
	#Create a decryption dictionary
	key_Decryption_Dictionary = dict(zip(new_Alphabet_Key, true_Alphabet)) #use zip to allow more than one string (arguments) to be paired together as one argument
	return ''.join(key_Decryption_Dictionary.get(letter.lower(), letter) for letter in ciphertext) #use .join to join all items from the dictionary into a string

#variables to hold the rsults from the functions
ciphertext = SS_Encryption(user_Input, new_Alphabet_Key, true_Alphabet)
decipher = SS_Decryption(user_Input, new_Alphabet_Key, true_Alphabet)

#If, Else statement to choose which process to cipher and print
if user_Selection == "E":
	print("Successfully Encrypted!")
	print("Your Plaintext input was:", user_Input)
	print("Your Key is:", new_Alphabet_Key)
	print("Your Ciphertext output is:", ciphertext)
 
    
elif user_Selection == "D":
	print("Successfully Decrypted!")
	print("Your Ciphertext input was:", user_Input)
	print("Your Key is:", new_Alphabet_Key)
	print("Your decrypted message is:", decipher)
	
else: 
	print("Error. You did not specify whether to encrypt or decrypt")
	
