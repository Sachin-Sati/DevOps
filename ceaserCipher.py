# def encrypt(text, s): 
#     result = ""

#     for i in range(len(text)):
#         char = text[i]
        
#         print(char.encode()[0])
#         print(ord(char))
#         if(char.isupper()):
#             result += chr((ord(char) + s - 65) % 26 + 65)
#         else:
#             result += chr((ord(char) + s - 97) % 26 + 97)
#     return result

# s = 3
# text = input("Enter a string: ")

# print("Plain Text: " + text)
# print("Ciphered Text: " + encrypt(text, s))



inp="ShivamBeast"
out=""
l=len(inp)
print("Input String : "+inp)

for i in range(0,l,2):
    out+=inp[i]
for i in range(1,l,2):
    out+=inp[i]

print("Encrypted Text Using railfence: "+out)