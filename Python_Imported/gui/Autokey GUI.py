#Autokey GUI and Cipher Tool

import tkinter as tk

#Set-up the window
window = tk.Tk()
window.title("Python Cipher Toolset - Autokey Cipher GUI")
window.geometry('500x500')
window.configure(background = '#000080')

#Global Variables
true_Alphabet = 'abcdefghijklmnopqrstuvwxyz'
AK_Plaintext = str(entry_User_Text.get())
AK_Key = entry_Key_Rule()

#Functions
def AK_Encryption(AK_Plaintext, AK_Key):
	AK_Ciphertext = [] #Create an empty list to store the Ciphertext
	list_Position = 0 #The ciphertext's list position starts at 0 and then moves 1 position for every iteration as long as many as it takes for the plaintext to be encrypted
	AK_Key = AK_Key.lower() #.lower() converts the key, and by extension the ciphertext, characters to lowercase letters
	for i in AK_Plaintext: #for loop to iterate through the plaintext
		AK_Plaintext = true_Alphabet.find(i.lower()) #.lower() converts i to lowercase values
		AK_Plaintext += true_Alphabet.find(AK_Key[list_Position]) #+= combines the two variables and assigns the result to AK_Plaintext
		AK_Key += i.lower() #+= combines the two variables and assigns the result to AK_Key
		AK_Plaintext %= len(true_Alphabet) # %= takes the modulus of the two variables and assigns the result to AK_Plaintext 
		list_Position += 1 #Moves the list position 1 value forward for every iteration of the for loop
		AK_Ciphertext.append(true_Alphabet[AK_Plaintext]) #Appends the list to the Ciphertext list
	return ''.join(AK_Ciphertext) #use .join to join all the values from the Ciphertext list into a string

#Encrypt Text Field
encrypt_Display = tk.Text(master=window, height=10, width = 50)
encrypt_Display.grid(column=1, row=4)
encrypt_Display.insert(tk.END, AK_Encryption)

#Create Main Label
label_Main = tk.Label(bg='gold', text='You are using the Autokey Cipher Tool')
label_Main.grid(column=0, row=0)

#Create User Text Input Label
label_User_Text = tk.Label(bg='gold', text='Input your text here')
label_User_Text.grid(column = 0, row=1)

#Create User Text Input Entry Box
entry_User_Text = tk.Entry()
entry_User_Text.grid(column=1, row = 1)

#Create Key Rule Label
label_Key_Rule = tk.Label(bg='gold', text='Insert your key')
label_Key_Rule.grid(column=0, row=2)

#Create Key Rule Entry Box
entry_Key_Rule = tk.Entry()
entry_Key_Rule.grid(column=1, row=2)

#Create Encrypt Button
button_Encrypt = tk.Button(bg='gold', text='Click to Encrypt') #, command=AK_Encryption)
button_Encrypt.grid(column=0, row=4)

window.mainloop()