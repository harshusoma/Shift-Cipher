import string

# Define alphabet
alpha= string.ascii_letters

#Encryption Function of plain text:
def encryption(plaintext,key):
    ciphertext=" "
    
# Iteration of each character through plaintext
    for character in plaintext:
        
#Get the value of the character in alphabet
        term=alpha.find(character)
        
#Shift the value with the help of key
        new_term= (term+key) % len(alpha)
        
#Addition of new character to ciphertext
        ciphertext += alpha[new_term]
    return ciphertext
        

#Decryption Function of cipher text:  
def decryption(ciphertext,key):
    plaintext=" "
    
# Iteration of each character through ciphertext
    for character in ciphertext:
        
#Get the value of the character in alphabet
        term=alpha.find(character)
        
#Reverse the value with the help of key
        new_term= (term-key) % len(alpha)
        
#Addition of new character to plaintext
        plaintext += alpha[new_term]
    return plaintext


#BruteForceAttack Function
def bruteforceattack(ciphertext):
    print("SET OF 26 PLAINTEXTS THAT CAN OCCUR ARE:")
    
#Trying all the possible keys
    for key in range(len(alpha)):
        plaintext = " "
        
#Iteration of each character through ciphertext
        for character in ciphertext:
            
#Get the value of the character in alphabet
            term=alpha.find(character)
            
#Decryption of the ciphertext with the current key
            new_term=(term - key) % len(alpha)
            
#Addition of Decrypted character
            plaintext += alpha[new_term]
            
#Print and Display the Plaintext and Key
        print(plaintext, " :: " , key)
        
    

#Main Menu    
while True:
    
#Printing the options for user to enter at the process of encryption,decryption
        print(" CHOOSE AN OPTION: ")
        print("1. ENCRYPTION: ")
        print("2. DECRYPTION: ")
        print("3. BRUTE FORCE ATTACK: ")
        print("4. QUIT")
        
        choice= input(" ENTER YOUR CHOICE [1/2/3/4]: ")
        

# This is part of Encryption option
        if choice == '1':
            plaintext = (input(" Enter Plaintext: "))
            key = int(input(" Enter Key: "))
            ciphertext = encryption(plaintext, key)
            print("The CipherText is:",ciphertext)
            

# This is part of the Decryption option     
        elif choice == '2':
            ciphertext = input(" Enter Ciphertext: ")
            key=int(input(" Enter Key: "))
            plaintext= decryption(ciphertext, key)
            print("The PlainText is:",plaintext)
            

#This is part of the BruteForceAttack option
        elif choice == '3':
            ciphertext = input(" Enter Ciphertext: ")
            print(" The Brute Force Attack Results are: ")
            bruteforceattack(ciphertext)
            

#Quit            
        elif choice == '4':
            print(" Quitting The Program!")
            break
            
# If the input is not matched with above options, this part is displayed         
        else:
            print(" Invalid Option. Please enter a correct option!!")
