#Custom Cipher Template
    
#READ ME FIRST!!!!
#Read through the entire code in order to understand what is occuring logic wise. With that said this is a simple template that will allow you to create a shift cipher that works based on any formula that produces an integer.
#You get to decide what formula the plaintext will be shifted by. The shift is limited in that it alphabetical characters can only be shifted a max of 26 times until further shifting wraps around the alphabet and back to
#the start. This means that a shift of 27 is equivalent to a shift of 1, similary to the Caesar cipher. This custom cipher template is not meant to create a complex encryption process but rather to give a simple to understand
#and customizable shift that can be decided by any formula the user decides. To create your own shift cipher with this template all you have to do is insert a formula into the parenthesis of round() in the
#custom_Shift_Formula variable found directly below. The round is needed to ensure that the formula always produces a whole number so do not remove it. Have Fun creating a shift cipher.


#Plaintext and Key variables
user_Input = str((input('Input your Plaintext:')))
custom_Shift_Formula = round() #keep round() function so that the shift will always be a whole number

def custom_Encryption(user_Input, custom_Shift_Formula):
	shifted_Ciphertext = "" #this is intentioanlly left blank so that the for loop and if/else statement below can return a value for it depending on the input and shift
	for letter in user_Input: # for loop to parse the input through the formulas below
		# Encrypt the uppercase letter of the plaintext
		# In order for isupper to be true, all characters must be uppercase, .isupper filters and keeps all uppercase letters in a string.
		if letter.isupper():
			# 65 is the ASCII unicode for the uppercase letter A, by adding 65 at the end of the fomrula, this ensures that encrypted letter's value always remains between 65(A), and 90(Z), and thus is uppercase.
			# Use the chr() method to return a string representing a character whose Unicode value is an integer.
			# Use the ord() fucntion to return an integer representing the Unicode Value
			# first we add the shift int the amount of letters we want to shift to the right, then we subtract 65 from the current letter value, then we modulo n by 26, and lastly we add 65 back to get its uppercase value.
			shifted_Ciphertext = shifted_Ciphertext + chr((ord(letter) + custom_Shift_Formula - 65) % 26 + 65)
        # Encrypt the lowercase letters of the plaintext
		# All other letter values that are not uppercase are lowercase, therefore we use else instead of .islower()
		else:
			#97 is the ASCII unicode for the lowercase letter a, by adding 97 at the end of the formula, this ensures that encrypted letter's value always remains between 97(a), and 122(z) and thus is lowercase.
			#first we subtract 97 from the current letter value, then we modulo n by 26, and lastly we add 97 back to get its lowercase value.
			shifted_Ciphertext = shifted_Ciphertext + chr((ord(letter) + custom_Shift_Formula - 97) % 26 + 97) 
		
	return shifted_Ciphertext
        

print("Your Input was: " + user_Input)
print("The Shift used after the formula computes is: ", (custom_Shift_Formula))
print("The Shifted Output is ", custom_Encryption(user_Input, custom_Shift_Formula)) #The cipher will remove spaces in the output