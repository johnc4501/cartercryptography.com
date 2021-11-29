#Caesar Cipher
    
''' Below is the mathematical encrption formula for the Caesar cipher:
Formula: e = (x + n) % 26, this forumla allows a shift to occur while always remaing between the values 0-25, a-z, respectively
Variable e = value of the encrypted letter resulted from the Caesar shift,
Variable x = value of plaintext letter,
Variable n = number of numeric shifts to the right x must go in order to achieve the desired Caesar shift,
(presuming n is added to x, use (x-n) to shift to the left or to decrypt a previous right shift)
'''
	
#Define Our Variables
caesar_Input = str((input('Input your Text for the Caesar Cipher:')))
#This is how many characters the alphabet will be shifted to create the new alphabet for the encrypted message to follow
caesar_Shift = int((input("Input Caesar Shift (Use a positive number to shift right and a negative number to shift left. You can also decrypt a message by shifting the opposite amount of what it was encrypted by):")))

#Define the Caesar Function
def caesar_Encryption(caesar_Input, caesar_Shift):
	caesar_Shifted = "" #this is intentioanlly left blank so that the for loop and if/else statement below can return a value for it depending on the input and caesar shift
	for letter in caesar_Input: # for loop to parse the input through the formulas below
		if letter == " ":
			caesar_Shifted = caesar_Shifted + letter
		# Encrypt the uppercase letter of the plaintext
		# In order for isupper to be true, all characters must be uppercase, .isupper filters and keeps all uppercase letters in a string.
		elif letter.isupper():
			# 65 is the ASCII unicode for the uppercase letter A, by adding 65 at the end of the fomrula, this ensures that encrypted letter's value always remains between 65(A), and 90(Z), and thus is uppercase.
			# Use the chr() method to return a string representing a character whose Unicode value is an integer.
			# Use the ord() fucntion to return an integer representing the Unicode Value
			# first we add the caesar shift int the amount of letters we want to shift to the right, then we subtract 65 from the current letter value, then we modulo n by 26, and lastly we add 65 back to get its uppercase value.
			caesar_Shifted = caesar_Shifted + chr((ord(letter) + caesar_Shift - 65) % 26 + 65)
        # Encrypt the lowercase letters of the plaintext
		# All other letter values that are not uppercase are lowercase, therefore we use else instead of .islower()
		else:
			#97 is the ASCII unicode for the lowercase letter a, by adding 97 at the end of the formula, this ensures that encrypted letter's value always remains between 97(a), and 122(z) and thus is lowercase.
			#first we subtract 97 from the current letter value, then we modulo n by 26, and lastly we add 97 back to get its lowercase value.
			caesar_Shifted = caesar_Shifted + chr((ord(letter) + caesar_Shift - 97) % 26 + 97) 
		
	return caesar_Shifted
        
#Print Our input, shift, and function results
print("Your Input was: " + caesar_Input)
print("The Caesar Shift used in the encryption/decryption is: ", (caesar_Shift)) #the str() method transforms all letter, integers, etc, into string format
print("The Caesar Shifted Output is ", caesar_Encryption(caesar_Input, caesar_Shift)) #the caesar_Encryption function is called
