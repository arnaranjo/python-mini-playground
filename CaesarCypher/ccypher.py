import os
import logo

os.system('cls' if os.name == 'nt' else 'clear')

print(logo.logo)

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
CONTINUE = True

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
    choice = input("Type 'E' to encrypt or type 'D' to decrypt a text:\n")
    while choice != 'E' and choice != 'D':
        choice = input("Please, type 'E' to encrypt or type 'D' to decrypt a text:\n")
    
    try:
        if choice == 'E':
            mainText = input("Type the text to encrypt: ").lower()
            step = int(input("Set the encryption number: ")) % len(ALPHABET)
            Encrypt(mainText, step)

        elif choice == 'D':
            mainText = input("Type the text to decrypt: ").lower()
            step = int(input("Set the encryption number: ")) % len(ALPHABET)
            Decrypt(mainText, step)
    except:
        print("The encryption number have to be a whole number.")
    
    selection = input("Type 'yes' if you want to use the app again. Otherwise type 'no':\n")
    while selection != 'yes' and selection != 'no':
        selection = input("Please, type 'yes' or 'no': ")
    if selection == 'no':
        CONTINUE = False
        print("Goodbye!")
 

