#Reverse GUI and Cipher Tool

import tkinter as tk

#Set-up the window
window = tk.Tk()
window.title("Python Cipher Toolset - Reverse Cipher GUI")
window.geometry('500x500')
window.configure(background = '#000080')

#Global Variables
original_Text = entry_User_Text.get()

#Functions
def reverse_Encryption(original_Text):
  return original_Text[::-1] # This slices through our variable by a step of -1, effecively reading our variable backwards and taking each element along as it goes

#Encrypt Text Field
encrypt_Display = tk.Text(master=window, height=10, width = 50)
encrypt_Display.grid(column=1, row=4)
encrypt_Display.insert(tk.END, reverse_Encryption)

#Create Main Label
label_Main = tk.Label(bg='gold', text='You are using the Reverse Cipher Tool')
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
button_Encrypt = tk.Button(bg='gold', text='Click to Encrypt') #, command=reverse_Encryption)
button_Encrypt.grid(column=0, row=4)

window.mainloop()