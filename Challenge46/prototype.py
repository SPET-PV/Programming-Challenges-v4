import string
# This is the beginning of the program
#Init
RawText = input("Enter your text :\n")
Char_Choice = input("What do you want to find :\n")
Total = 0
# Treatment
for i in range(0,len(RawText)):
    if RawText[i] == Char_Choice:
        Total += 1
# Output
print(f"The Number of Occurences of this Character is :\"{Total}\"")