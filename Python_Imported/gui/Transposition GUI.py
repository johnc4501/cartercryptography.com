#Columnar Transposition GUI and Cipher Tool

import tkinter as tk

#Set-up the window
window = tk.Tk()
window.title("Python Cipher Toolset - Columnar Transposition Cipher GUI")
window.geometry('500x500')
window.configure(background = '#000080')

#Global Variables
trans_Plaintext = str(entry_User_Text.get())
position_Key = entry_Key_Rule()

#Functions
def columnar_Transposition_Encryption(position_Key, trans_Plaintext):

    def rows_Cols(sequence, length):
        return [sequence[i:i + length] for i in range(0, len(sequence), length)] #Takes the plaintext and reogranizes it into an orded sequence of rows depending on the length of the key creating a matrix
	
	#The new_Sequence dictionary is determined by the integer's value. The lowest integer will have it's column's letters appear first in the sequence.
    new_Sequence = {int(val): i for i, val in enumerate(position_Key)} #Use dictionary comprehension to establish i for i, use the int() method to restrict val to only contain integer values, use the enumerate() method to loop over an iterable object.

    ciphertext = '' #This is intentioanlly left blank so that the for loops below can return a value for it depending on the key
    for i in sorted(new_Sequence.keys()): #The keys() method returns the keys of the dictionary as a list. Sorted() organizes the list of order's keys
        for position in rows_Cols(trans_Plaintext, len(position_Key)): #the plaintext and key variables are used as the sequence and length function arguments. 
            try:
                ciphertext += position[new_Sequence[i]] #+= combines the two
            except: #allows spaces to remain in the cipheretext
                continue

    return ciphertext

#Encrypt Text Field
encrypt_Display = tk.Text(master=window, height=10, width = 50)
encrypt_Display.grid(column=1, row=4)
encrypt_Display.insert(tk.END, columnar_Transposition_Encryption)

#Create Main Label
label_Main = tk.Label(bg='gold', text='You are using the Columnar Transposition Cipher Tool')
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
button_Encrypt = tk.Button(bg='gold', text='Click to Encrypt') #, command=columnar_Transposition_Encryption)
button_Encrypt.grid(column=0, row=4)

window.mainloop()