alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encrypt_msg = ""
decrypt_msg = ""
def encryption(msg,shift):
    global encrypt_msg
    for i in msg:
        pos = alphabet.index(i)
        new_pos = (pos + shift) % 26
        j = alphabet[new_pos]
        encrypt_msg +=j
    print(encrypt_msg)
        
def decryption(msg,shift):
    global decrypt_msg
    for i in msg:
        pos = alphabet.index(i)
        new_pos = (pos - shift) % 26
        j = alphabet[new_pos]
        decrypt_msg +=j
    print(decrypt_msg)
    
    
is_on = True
while is_on:
    inputs = input("Type 'encrypt' for encryption, type 'decrypt' for decryption:").lower()
    msg = input("Type your message:")
    shift = int(input("Type the shift number:"))
    if inputs == 'encrypt':
        encryption(msg,shift)
    elif inputs == 'decrypt':
        decryption(msg,shift)
    else:
        print("Please write correct option")
    is_= int(input("Type '1' if you want to go again ohterwise type '0':"))
    if is_ == 0:
        break
    
print("Thank you")