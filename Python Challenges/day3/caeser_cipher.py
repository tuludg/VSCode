from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

choice_mode = input("Type 'encode' to encrypt and 'decode' to : \n").lower()
text = input("Type your message here: \n").lower()
shift = int(input("Type the shift number: \n"))


# TODO-1. Create a function called encrypt that takes the text and 
# shift amounts as parameters and shifts each letter by the shift number

def encrypt(message, shift_num):
    new_text = ""
    identifier = 0
    for letter in message:
        if letter in alphabet:
            identifier = alphabet.index(letter)
            new_index = (identifier + shift_num) % 26
            new_text += alphabet[new_index]
        else:
            new_text += letter
            
       
            
    return new_text


secret_message = encrypt(text, shift)
print(secret_message)
        
        

