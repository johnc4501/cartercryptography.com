#Letter-Number GUI and Cipher Tool

import tkinter as tk

#Set-up the window
window = tk.Tk()
window.title("Python Cipher Toolset - Letter-Number Cipher GUI")
window.geometry('500x500')
window.configure(background = '#000080')

#Global Variables
LN_Plaintext = str(entry_User_Text.get())

#Functions
def LN_Encryption(LN_Plaintext):
    LN_Ciphertext = [] #Create a List that will store the Ciphertext data, which appear as numbers converted from the letters of our plaintext strings
	
    for i in LN_Plaintext.lower(): #For loop to iterate though the plaintext. Lower() ensures that a capital letter and lowercase appear as the same ASCII value in the ciphertext. 
        i = ord(i) - 96 #Use the ord() fucntion to return an integer representing the Unicode Value and then subtract 96 to get the ASCII value. Blank spaces appear as -64 in the ciphertext.
        LN_Ciphertext.append(i) #Append the looped values from the plaintext into the Ciphertext list. 
    
    return(LN_Ciphertext)
	
#Encrypt Text Field
encrypt_Display = tk.Text(master=window, height=10, width = 50)
encrypt_Display.grid(column=1, row=4)
encrypt_Display.insert(tk.END, LN_Encryption)
 
#Create Main Label
label_Main = tk.Label(bg='gold', text='You are using the Letter-Number Cipher Tool')
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
button_Encrypt = tk.Button(bg='gold', text='Click to Encrypt') #, command=LN_Encryption)
button_Encrypt.grid(column=0, row=4)

window.mainloop()