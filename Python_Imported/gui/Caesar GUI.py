#Caesar GUI and Cipher Tool

import tkinter as tk
#Set-up the window
window = tk.Tk()
window.title("Python Cipher Toolset - Caesar Shift Cipher GUI")
window.geometry('500x500')
window.configure(background = '#000080')
#Global Variables
caesar_Input = str(entry_User_Text.get())
caesar_Shift = int(entry_Key_Rule())
#Functions
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
#Encrypt Text Field
encrypt_Display = tk.Text(master=window, height=10, width = 50)
encrypt_Display.grid(column=1, row=4)
encrypt_Display.insert(tk.END, caesar_Encryption)
 
#Create Main Label
label_Main = tk.Label(bg='gold', text='You are using the Caesar Shift Cipher Tool')
label_Main.grid(column=0, row=0)

#Create User Text Input Label
label_User_Text = tk.Label(bg='gold', text='Input your text here')
label_User_Text.grid(column = 0, row=1)

#Create User Text Input Entry Box
entry_User_Text = tk.Entry()
entry_User_Text.grid(column=1, row = 1)

#Create Key Rule Label
label_Key_Rule = tk.Label(bg='gold', text='Insert your key rule')
label_Key_Rule.grid(column=0, row=2)

#Create Key Rule Entry Box
entry_Key_Rule = tk.Entry()
entry_Key_Rule.grid(column=1, row=2)

#Create Encrypt Button
button_Encrypt = tk.Button(bg='gold', text='Click to Encrypt') #, command=caesar_Encryption)
button_Encrypt.grid(column=0, row=4)

window.mainloop()