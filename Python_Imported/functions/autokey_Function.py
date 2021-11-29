#Autokey Function

#Define our Variables
true_Alphabet = 'abcdefghijklmnopqrstuvwxyz'
AK_Plaintext = input('Input your Plaintext: ')
AK_Key = input('Input your key: ')

#Define Encryption Function
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

#Variable to store the results of the function
AK_Encryption_Results = AK_Encryption(AK_Plaintext, AK_Key)

#Print our results
print("Successfully Encrypted!")
print("Your Plaintext input was:", AK_Plaintext)
print("Your Key is:", AK_Key)
print("Your Ciphertext output is:", AK_Encryption_Results)
