encryptimport string

def get_key():
    key = int(input("Enter your key (interger) here: "))
    return key


def get_message():
    message = input("Enter the message here: ")
    return message

def encrypt(message, key):  
    encrypted_message = ""
    for letter in message:
        if letter in string.ascii_uppercase:
            old_ascii = ord(letter)
            new_ascii = (old_ascii + key - 65) % 26 + 65
            new_char = chr(new_ascii)
            encrypted_message += new_char
        elif letter in string.ascii_lowercase:  
            old_ascii = ord(letter)
            new_ascii = (old_ascii + key - 97) % 26 + 97
            new_char = chr(new_ascii)
            encrypted_message += new_char
        else:
            old_ascii = ord(letter)
            new_ascii = old_ascii
            new_char = chr(new_ascii)
            encrypted_message += new_char
    encrypted_message
    return encrypted_message


def decrypt(message, key):  # UPPGIFT 4
    decrypted_message = ""
    for letter in message:
        if letter in string.ascii_uppercase:
            old_ascii = ord(letter)
            new_ascii = (old_ascii - key - 65) % 26 + 65
            new_char = chr(new_ascii)
            decrypted_message += new_char
        elif letter in string.ascii_lowercase:
            old_ascii = ord(letter)
            new_ascii = (old_ascii - key - 97) % 26 + 97
            new_char = chr(new_ascii)
            decrypted_message += new_char
        else:
            old_ascii = ord(letter)
            new_ascii = old_ascii
            new_char = chr(new_ascii)
            decrypted_message += new_char
    decrypted_message
    return decrypted_message

def break_crypt(message):
    for key in range(1,26):
        decrypted_message = decrypt(message, key)
        print(decrypted_message)
        
          

def action():
    import string
    while True:
        print("What would you like to do?")
        choice = input("e: encrypt\nd: decrypt\nb: break\nq: quit\n> ")

        if choice.lower() == "q":
            break

        elif choice.lower() == "d":
            message = get_message()
            key = get_key()
            plaintext = decrypt(message, key)
            print("The decrypted message is %s" % plaintext)
        elif choice.lower() == "e":
            message = get_message()
            key = get_key()
            cryptotext = encrypt(message, key)
            print("The encrypted message is %s" % cryptotext)
        elif choice.lower() == "b":
            message = get_message()
            break_crypt(message)


action()
