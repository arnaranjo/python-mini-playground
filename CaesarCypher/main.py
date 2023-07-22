import logo
import os
from ccypher import CCypher
from gui import AppGUI

def main():
    
    KEEPON = True
    newCypher = CCypher()
    newCypher.DefineAlphabet()

    while KEEPON:
        choice = input("Type 'E' to encrypt or type 'D' to decrypt a text: ")
        while choice != 'E' and choice != 'D':
            choice = input("Please, type 'E' to encrypt or type 'D' to decrypt a text: ")
        
        try:
            if choice == 'E':
                mainText = input("Type the text to encrypt: ")
                step = int(input("Set the encryption number: "))
                newCypher.Encrypt(mainText, step)

            elif choice == 'D':
                mainText = input("Type the text git: ")
                step = int(input("Set the encryption number: "))
                newCypher.Decrypt(mainText, step)
        except:
            print("Error with the character.")
        
        selection = input("Type 'yes' if you want to use the app again. Otherwise type 'no': ")
        while selection != 'yes' and selection != 'no':
            selection = input("Please, type 'yes' or 'no': ")
        if selection == 'no':
            KEEPON = False
            print("Goodbye!")    

#--------------------------------------------------------------#

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo.logo)
    # main()
    newGUI = AppGUI()