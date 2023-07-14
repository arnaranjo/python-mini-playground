import os
import logo

os.system('cls' if os.name == 'nt' else 'clear')

print(logo.logo)

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def CodeText(mainText, step):
    textCoded = ""
    for lt in mainText:
        newIndex = ALPHABET.index(lt) + step
        if lt in ALPHABET:
            textCoded += ALPHABET[ALPHABET.index(lt)+ step if newIndex <= len(ALPHABET) else step - 1]
            # If the new position is out of the range, it starts from the beginning. 
        else:
            textCoded += "-"
    return textCoded


mainText = input("Text to encrypt: ")
step = int(input("Set the encryption number: "))
print(CodeText(mainText,step))
