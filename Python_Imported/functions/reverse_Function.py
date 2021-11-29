#Reverse Cipher


#Define our Variables
original_Text = input('Input your plaintext to reverse or ciphertext to decrypt: ')

#Define our Reverse Function
def reverse_Encryption(original_Text):
  return original_Text[::-1] # This slices through our variable by a step of -1, effecively reading our variable backwards and taking each element along as it goes

#Print our Function results
print(reverse_Encryption(original_Text))