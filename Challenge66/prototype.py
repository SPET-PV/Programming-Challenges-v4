import string

#Inputs
RawText = input("Enter your text : \n")
HexOutput = []
BinOutput = []
OctOutput = []
#Treatment
for i in range(0,len(RawText)):
    HexOutput.append(hex(ord(RawText[i])))
    BinOutput.append(bin(ord(RawText[i])))
    OctOutput.append(oct(ord(RawText[i])))
HEX = " ".join(HexOutput)
BIN = " ".join(BinOutput)
OCT = " ".join(OctOutput)
#Output
print(f"\nHexadecimal : \n{HEX}")
print(f"\nBinary : \n{BIN}")
print(f"\nOctal : \n{OCT}")
