alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input ("type 'encode to encrypt, type 'decode' to decrypt:\n " )
text = input ( "Type ypur message: \n ").lower()
shift = int(input("type the shift number: \n"))

def encrypt(text , shift)
    for i in text:
        