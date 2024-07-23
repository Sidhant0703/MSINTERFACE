#importing prerequesties
import string

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    # Traverse text
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's not a letter, add it as is
        else:
            result += char

    return result

# ASCII Art
ascii_art = """
   ____ ____    _____ ___   ___  _          _  _____ _____ 
  / ___/ ___|  |_   _/ _ \ / _ \| |        | |/ /_ _|_   _|
 | |  | |   _____| || | | | | | | |   _____| ' / | |  | |  
 | |__| |__|_____| || |_| | |_| | |__|_____| . \ | |  | |  
  \____\____|    |_| \___/ \___/|_____|    |_|\_\___| |_|  
                                                           
          Caesar Cipher Tool by Sidhanta Palei
"""

print(ascii_art)

# Get user input for mode, text, and shift
mode = input("Do you want to (e)ncrypt or (d)ecrypt? ").strip().lower()
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))

if mode == 'e':
    mode = 'encrypt'
    result = caesar_cipher(text, shift, mode)
    print(f"Encrypted Text: {result}")
elif mode == 'd':
    mode = 'decrypt'
    result = caesar_cipher(text, shift, mode)
    print(f"Decrypted Text: {result}")
else:
    print("Invalid option selected. Please choose 'e' to encrypt or 'd' to decrypt.")
