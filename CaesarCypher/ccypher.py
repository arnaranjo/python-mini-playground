import os
import pandas as pn
import logo

os.system('cls' if os.name == 'nt' else 'clear')

print(logo.logo)

CONTINUE = True
DATA_FILE = "CaesarCypher/character.txt"
ALPHABET = []

# # Generate a list from the file content.
with open(file=DATA_FILE, mode='r',encoding="utf-8") as data:
    ALPHABET = data.read().rsplit()


def Encrypt(mainText, step):
    texEncrypted = ""
    for lt in mainText:
        newIndex = ALPHABET.index(lt) + step
        if lt in ALPHABET:
            texEncrypted += ALPHABET[newIndex if newIndex < len(ALPHABET) else newIndex - len(ALPHABET)]
        # If the new position is out of the range, it will set the new index from the beginning. 
    print(f"The text encrypted is: {texEncrypted}")


def Decrypt(mainText, step):
    textDecrypted = ""
    for lt in mainText:
        newIndex = ALPHABET.index(lt) - step
        if lt in ALPHABET:
            textDecrypted += ALPHABET[newIndex if newIndex >= 0 else len(ALPHABET) + newIndex]
        # If the new position is out of the range, it will set the index from the end of the list because newIndex is negative. 
    print(f"The text decrypted is: {textDecrypted}")


while CONTINUE:
    choice = input("Type 'E' to encrypt or type 'D' to decrypt a text: ")
    while choice != 'E' and choice != 'D':
        choice = input("Please, type 'E' to encrypt or type 'D' to decrypt a text: ")
    
    try:
        if choice == 'E':
            mainText = input("Type the text to encrypt: ")
            step = int(input("Set the encryption number: ")) % len(ALPHABET)
            Encrypt(mainText, step)

        elif choice == 'D':
            mainText = input("Type the text git: ")
            step = int(input("Set the encryption number: ")) % len(ALPHABET)
            Decrypt(mainText, step)
    except:
        print("Error with the character.")
    
    selection = input("Type 'yes' if you want to use the app again. Otherwise type 'no': ")
    while selection != 'yes' and selection != 'no':
        selection = input("Please, type 'yes' or 'no': ")
    if selection == 'no':
        CONTINUE = False
        print("Goodbye!")