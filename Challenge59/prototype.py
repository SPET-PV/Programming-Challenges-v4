import string

#mop = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

LETTERS = {' ' : 'space','a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9, 'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25}
REVERSE = {'space' : ' ', 0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd', 4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h', 8 : 'i', 9 : 'j', 10 : 'k', 11 : 'l', 12 : 'm', 13 : 'n', 14 : 'o', 15 : 'p', 16 : 'q', 17 : 'r', 18 : 's', 19 : 't', 20 : 'u', 21 : 'v', 22 : 'w', 23 : 'x', 24 : 'y', 25 : 'z'}

print("This a Simple Shift+3 Ceasar Code (Encryptor- Decryptor)")
Choice = input("What do you want to do :\n(1) - Encrypt\n(2) - Decrypt\n")


def Encryption():
    #Local Declarations
    PlainText = input("Enter your text :\n")
    PlainText = PlainText.lower()
    Encoded = []
    Encrypted = []
    Decoded = []
    Cypher = ""
    #Encoding
    for i in range(0,len(PlainText)):
        Encoded.append(LETTERS[f'{PlainText[i]}'])
    #Encryption
    for i in range(0,len(Encoded)):
        if Encoded[i] == 'space':
            Encrypted.append('space')
        else:
            Encrypted.append((Encoded[i] +  3) % 26)
    #Decoding
    for i in range(0,len(Encrypted)):
        Decoded.append(REVERSE[Encrypted[i]])
    for j in range(0,len(Encrypted)):
        Cypher = ''.join(Decoded)
    #Output
    print(f"\nYour Cypher is :\n{Cypher.upper()}")

def Decryption():
    #Local Declarations
    Cypher = input("Enter your Cypher :\n")
    Cypher = Cypher.lower()
    Encoded = []
    Encrypted = []
    Decoded = []
    PlainText = ""
    #Encoding
    for i in range(0,len(Cypher)):
        Encoded.append(LETTERS[f'{Cypher[i]}'])
    #Encryption
    for i in range(0,len(Encoded)):
        if Encoded[i] == 'space':
            Encrypted.append('space')
        else:
            Encrypted.append((Encoded[i] -  3) % 26)
    #Decoding
    for i in range(0,len(Encrypted)):
        Decoded.append(REVERSE[Encrypted[i]])
    for j in range(0,len(Encrypted)):
        PlainText = ''.join(Decoded)
    #Output
    print(f"\nYour Text is :\n{PlainText}")

#Choice

if Choice == '1':
    Encryption()
elif Choice == '2':
    Decryption()
else:
    print("Wrong Entry !")