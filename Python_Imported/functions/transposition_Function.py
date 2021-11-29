#Columnar Transposition Cipher


# How the key works: 
# The key is an order of integers chosen by the user. The plaintext is rewritten below those integers using the length of integers as the amount of columns.
# Example: plaintext = Georgia, key = 312

# 312
# Geo
# rgi
# a

# For Encryption the sequence of characters is reordered by the using the lowest value integer's column of characters as the beginning of the ciphertext
# then the next lowest value integer's column of characters is added to the ciphertext, and so on until the highest value integer is finished.
# Ciphertext for the example above will read as such (Column 1:eg) + (column 2: oi) + (column 3: Gra). Final Ciphertext reads as egoiGra

#Define our Variables
trans_Plaintext = input('Input your Plaintext for the Columnar Transposition Cipher: ')
position_Key = input('Insert your key as an integer: ')

#Define our Columnar Transposition Function
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

#Print the completed function to get the Ciphertext
print("Your Plaintext was: ", trans_Plaintext)
print("Your Key is: ", position_Key)
print("Columnar Transposition Ciphertext: ", columnar_Transposition_Encryption(position_Key, trans_Plaintext))
