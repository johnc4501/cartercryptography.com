#Vertical GUI and Cipher Tool

import tkinter as tk

#Set-up the window
window = tk.Tk()
window.title("Python Cipher Toolset - Vertical Cipher GUI")
window.geometry('500x500')
window.configure(background = '#000080')

#Global Variables
vertical_Plaintext = str(entry_User_Text.get())
rows_Key = int(entry_Key_Rule())

#Functions
def vertical_Encryption(vertical_Plaintext, rows_Key):
    return [vertical_Plaintext[i::rows_Key] for i in range(rows_Key)] #Using list comprehension, slicing, and the range function we slice the plaintext into the amount of rows specified by the key


#Encrypt Text Field
encrypt_Display = tk.Text(master=window, height=10, width = 50)
encrypt_Display.grid(column=1, row=4)
encrypt_Display.insert(tk.END, vertical_Encryption)
 
#Create Main Label
label_Main = tk.Label(bg='gold', text='You are using the Vertical Cipher Tool')
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
button_Encrypt = tk.Button(bg='gold', text='Click to Encrypt') #, command=vertical_Encryption)
button_Encrypt.grid(column=0, row=4)

window.mainloop()