import os
import logo
os.system('cls' if os.name == 'nt' else 'clear')

class CCypher:
    def __init__ (self, dataFile, alphabet):
        self.dataFile = "CaesarCypher/character.txt"
        self.alphabet = []


    def DefineAlphabet(self):
        # Generate a list from the file content.
        with open(file=self.dataFile, mode='r',encoding="utf-8") as data:
            self.alphabet = data.read().rsplit()


    def Encrypt(self, mainText, step):
        texEncrypted = ""
        for lt in mainText:
            newIndex = self.alphabet.index(lt) + step
            if lt in self.alphabet:
                texEncrypted += self.alphabet[newIndex if newIndex < len(self.alphabet) else newIndex - len(self.alphabet)]
            # If the new position is out of the range, it will set the new index from the beginning. 
        print(f"The text encrypted is: {texEncrypted}")


    def Decrypt(self, mainText, step):
        textDecrypted = ""
        for lt in mainText:
            newIndex = self.alphabet.index(lt) - step
            if lt in self.alphabet:
                textDecrypted += self.alphabet[newIndex if newIndex >= 0 else len(self.alphabet) + newIndex]
            # If the new position is out of the range, it will set the index from the end of the list because newIndex is negative. 
        print(f"The text decrypted is: {textDecrypted}")


#--------------------------------------------------------------#

print(logo.logo)
KEEPON = True
newCypher = CCypher()

while KEEPON:
    choice = input("Type 'E' to encrypt or type 'D' to decrypt a text: ")
    while choice != 'E' and choice != 'D':
        choice = input("Please, type 'E' to encrypt or type 'D' to decrypt a text: ")
    
    try:
        if choice == 'E':
            mainText = input("Type the text to encrypt: ")
            step = int(input("Set the encryption number: ")) % len(newCypher.alphabet)
            newCypher.Encrypt(mainText, step)

        elif choice == 'D':
            mainText = input("Type the text git: ")
            step = int(input("Set the encryption number: ")) % len(newCypher.alphabet)
            newCypher.Decrypt(mainText, step)
    except:
        print("Error with the character.")
    
    selection = input("Type 'yes' if you want to use the app again. Otherwise type 'no': ")
    while selection != 'yes' and selection != 'no':
        selection = input("Please, type 'yes' or 'no': ")
    if selection == 'no':
        KEEPON = False
        print("Goodbye!")