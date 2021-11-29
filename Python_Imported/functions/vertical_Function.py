#Vertical Cipher

#Define our Variables
vertical_Plaintext = input("Input your plaintext for the Vertical Cipher: ") #spaces in the plaintext will appear as spaces in the ciphertext as well
rows_Key = int(input("Input your key as an intger, specifying the amount of rows the ciphertext will be grouped in: "))

#Define Vertical Cipher Function
def vertical_Encryption(vertical_Plaintext, rows_Key):
    return [vertical_Plaintext[i::rows_Key] for i in range(rows_Key)] #Using list comprehension, slicing, and the range function we slice the plaintext into the amount of rows specified by the key

#Create a variable to store the function results
vertical_Ciphertext = vertical_Encryption(vertical_Plaintext, rows_Key)

#Print the function results
print(vertical_Ciphertext)
#When printed the ciphertext will be grouped into the amount of rows the the user specifies in the key. While this cipher is the vertcial cipher, 
#Python prints the list and the list values in horitzontal order, however when the list's groups of strings are stacked vertically they can be read top to bottom and left to right and the ciphertext will be legible.
