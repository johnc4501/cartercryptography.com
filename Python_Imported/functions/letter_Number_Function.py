#Letter-number Cipher


#Define Our Variables
LN_Plaintext = input("Input your Plaintext for the Letter-Number Cipher: ")

def LN_Encryption(LN_Plaintext):
    LN_Ciphertext = [] #Create a List that will store the Ciphertext data, which appear as numbers converted from the letters of our plaintext strings
	
    for i in LN_Plaintext.lower(): #For loop to iterate though the plaintext. Lower() ensures that a capital letter and lowercase appear as the same ASCII value in the ciphertext. 
        i = ord(i) - 96 #Use the ord() fucntion to return an integer representing the Unicode Value and then subtract 96 to get the ASCII value. Blank spaces appear as -64 in the ciphertext.
        LN_Ciphertext.append(i) #Append the looped values from the plaintext into the Ciphertext list. 
    
    return(LN_Ciphertext)
    
print(LN_Encryption(LN_Plaintext))