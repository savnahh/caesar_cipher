print("Savona Shrestha (233077)")
print()
def encrypt(key, message): #this is encrypt function
    message = message.upper() #defines message varaible
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #defines the alphabet
    result = "" 
    for letter in message: 
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) + key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter
    return result

def decrypt(key, message): #decrypt function
    message = message.upper() #defines message varaible
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # defines the alphabet
    result = ""
    for letter in message: 
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter
    return result

def welcome():
        print("Welcome to the Caesar Cipher. This program encrypts and decrypts text with Caesar Cipher")

def enter_message():
    user = input("Would you like to encrypt"+ "(" + "e"+  ")" + "or decrypt" + "(" + "d"+  ")? =") 
    if user =="e":
        user_message = input("What message would you like to encrypt:")
        user_shift_key = int(input("What is the shift number:"))
        cipher_text = encrypt(user_shift_key, user_message)
        print(f"Cipher Text: {cipher_text}")
        
    elif user =="d":
        user_message = input("What message would you like to decrypt:")
        user_shift_key = int(input("What is the shift number:"))
        cipher_text = decrypt(user_shift_key, user_message)
        print(f"Cipher Text: {cipher_text}")
        
    else:
        print("Invalid Mode")
        
def messageagain():
        useragain = input("Would you like to encrypt or decrypt another message? (y/n)") 
        if useragain.upper() == "Y":
            enter_message();
        else:
            print("Thank you for using the program, goodbye")

welcome()
enter_message()
messageagain()
   
# checking if the encrypt or decrypt is working or 📓 

# def main():
    #     word = "BILLY"

#     #encrypt "BILLY" with a key of 3
#     encrypted = encrypt(3,word)
#     print(encrypted) #should print "ELOOB"

#     #decrypt "ELOOB" with a key of 3
#     decrypted = decrypt(3,encrypted)
#     print(decrypted) #should print "BILLY"

# if __name__ == "__main__":
#     main()
