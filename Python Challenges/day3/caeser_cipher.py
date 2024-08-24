from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def casesar_cipher():
    
    go_on = "yes"
         
# TODO-1. Create a function called encrypt that takes the text and 
# shift amounts as parameters and shifts each letter by the shift number

    def encrypt(message, shift_num):

                new_text = ""
                identifier = 0
                
 # looping through text to shift them into desired amount           
                for letter in message:
                    if letter in alphabet:
                        identifier = alphabet.index(letter)
                        new_index = (identifier + shift_num) % len(alphabet)
                        new_text += alphabet[new_index]
                    else:
                        new_text += letter
                print(f"This is your secret message: {new_text}")
        

    # TODO-2. Create a decode function that decrypts the  secret message
    def decode(message, shift_num):
        
        decrypted_text = ""
        identifier = 0        

        for char in message:
            if char in alphabet:
                identifier = alphabet.index(char)
                identifier -= shift_num
                if identifier < 0:
                    identifier += len(alphabet)
                    decrypted_text += alphabet[identifier]
                else:
                    decrypted_text +=  alphabet[identifier]
            else:
                decrypted_text += char
                
        print(f"Here is the decrypted message: {decrypted_text}")


    while go_on != "no":
        
        choice_mode = input("Type 'encode' to encrypt and 'decode' to : \n").lower()
        text = input("Type your message here: \n").lower()
        shift = int(input("Type the shift number: \n"))

        if choice_mode == "encode":
            encrypt(text, shift)
        elif choice_mode == "decode":
            decode(text, shift)
            
    
        go_on = input("Type 'yes if you want to continue and 'no' when you want to terminate the process")


casesar_cipher()
            
        
            
            



            
            

