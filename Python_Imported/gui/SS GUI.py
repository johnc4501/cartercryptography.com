#Simple Substitution GUI and Cipher Tool

import tkinter as tk

#Set-up the window
window = tk.Tk()
window.title("Python Cipher Toolset - Simple Substitution Cipher GUI")
window.geometry('500x500')
window.configure(background = '#000080')

#Global Variables
true_Alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_Alphabet_Key = str(entry_Key_Rule.get())
user_input = str(entry_User_Text.get())
ciphertext = SS_Encryption(user_Input, new_Alphabet_Key, true_Alphabet)
decipher = SS_Decryption(user_Input, new_Alphabet_Key, true_Alphabet)

#Functions
def SS_Encryption(user_Input, new_Alphabet_Key, true_Alphabet):
	#Create an encryption dictionary
	key_Encryption_Dictionary = dict(zip(true_Alphabet, new_Alphabet_Key)) #use zip to allow more than one string (arguments) to be paired together as one argument
	return ''.join(key_Encryption_Dictionary.get(letter.lower(), letter) for letter in user_Input) #use .join to join all items from the dictionary into a string

def SS_Decryption(ciphertext, new_Alphabet_Key, true_Alphabet):
	#Create a decryption dictionary
	key_Decryption_Dictionary = dict(zip(new_Alphabet_Key, true_Alphabet)) #use zip to allow more than one string (arguments) to be paired together as one argument
	return ''.join(key_Decryption_Dictionary.get(letter.lower(), letter) for letter in ciphertext) #use .join to join all items from the dictionary into a string

#Encrypt Text Field
encrypt_Display = tk.Text(master=window, height=10, width = 50)
encrypt_Display.grid(column=1, row=4)
encrypt_Display.insert(tk.END, SS_Encryption)

#Decrypt Text Field
encrypt_Display = tk.Text(master=window, height=10, width = 50)
encrypt_Display.grid(column=1, row=6)
encrypt_Display.insert(tk.END, SS_Decryption)

#Create Main Label
label_Main = tk.Label(bg='gold', text='You are using the Simple Substitution Cipher Tool')
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
button_Encrypt = tk.Button(bg='gold', text='Click to Encrypt') #, command=SS_Encryption)
button_Encrypt.grid(column=0, row=4)

#Create Decrypt Button
button_Decrypt = tk.Button(bg='gold', text='Click to Decrypt') #, command=SS_Decryption)
button_Decrypt.grid(column=0, row=6)

window.mainloop()
