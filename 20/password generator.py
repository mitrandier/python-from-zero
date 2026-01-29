print("Welcome to the Pypassword Generator!")

import random

letters_num = int(input("How many letters would you like in your password?\n"))
number_num= int(input("How many numbers would you like?\n"))
symbols_num= int(input("How many symbols would you like?\n"))

letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
          'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
numbers=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols=['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']


password = []
for i in range (0,letters_num):
    password.append(random.choice(letters))
for i in range (0,number_num):
    password.append(random.choice(numbers))
for i in range (0,symbols_num):
    password.append(random.choice(symbols))

pass1 =''.join(password)
print(password)
print(pass1)
    
    