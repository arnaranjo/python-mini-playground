'''
CLASS CCypher:
    Performs encryption and decryption of a string according to the Caesar cipher
    It uses an external source of characters and as input the number of steps and the string.
    (https://en.wikipedia.org/wiki/Caesar_cipher)
'''

class CCypher:
    def __init__ (self):
        
        self.dataFile = "CaesarCypher/character.txt"
        self.alphabet = []
        
        self.DefineAlphabet()

    def DefineAlphabet(self):
        with open(file=self.dataFile, mode='r',encoding="utf-8") as data:
            self.alphabet = data.read().rsplit()
                # .rsplit(separator, maxsplit) This method splits a string into a list.

    def Encrypt(self, mainText, step):
        texEncrypted = ""
        for lt in mainText:
            newIndex = self.alphabet.index(lt) + (step % len(self.alphabet))
            if lt in self.alphabet:
                texEncrypted += self.alphabet[newIndex if newIndex < len(self.alphabet) else newIndex - len(self.alphabet)]
            # If the new position is out of the range, it will set the new index from the beginning. 
        return texEncrypted

    def Decrypt(self, mainText, step):
        textDecrypted = ""
        for lt in mainText:
            newIndex = self.alphabet.index(lt) - (step % len(self.alphabet))
            if lt in self.alphabet:
                textDecrypted += self.alphabet[newIndex if newIndex >= 0 else len(self.alphabet) + newIndex]
            # If the new position is out of the range, it will set the index from the end of the list because newIndex is negative. 
        return textDecrypted