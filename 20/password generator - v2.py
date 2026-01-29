print("Welcome to the Pypassword Generator!")

import random

letters = input("111How many letters would you like in your password?\n")
numbers = input("222How many numbers would you like?\n")
symbols = input("333How many symbols would you like?\n")

print(letters)
print(numbers)
print(symbols)

letters_num = int(input("How many letters would you like in your password?\n"))
number_num = int(input("How many numbers would you like?\n"))
symbols_num = int(input("How many symbols would you like?\n"))

print("inpus:",symbols_num, number_num, number_num)

sum1 = symbols_num + number_num + letters_num

print("sum1:",sum1)

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
#            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
#            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
#            'Y', 'Z']
# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']

 
 
                    
letters1 = letters.split(' ')
numbers1 = numbers.split(' ')
symbols1 = symbols.split(' ')

print(type(letters))
print(type(letters1))
print(type(numbers))
print(type(numbers1))
print(type(symbols))
print(type(symbols1))
        

password = []
print("password1: ",password)

random = random.randint(0,2)
print("random:",random)
 
a = letters_num
b = number_num
c = symbols_num

if random == 0 and a != 0:
    #for i in range (0,1):
    password = random.choice(letters1)
    print("password a:" ,password)
    a -= 1
    print("a=",a)
        
elif random == 1 and b != 0:
    #for j in range (0,1):
    password = random.choice(numbers1)
    print("password b :" ,password)
    b -= 1
    print("b=",b)
        
elif random == 2 and c != 0:    
    #for k in range (0,1):
    password = random.choice(symbols1)
    print("password c :" ,password)
    c -= 1
    print("c=",c)

print("the final passwor:", password)
final_password = password.join(password)
print("the exit is:" , final_password)


# 
# for i in range (0,letters_num):
#     password.append(random.choice(letters))
# for i in range (0,number_num):
#     password.append(random.choice(numbers))
# for i in range (0,symbols_num):
#     password.append(random.choice(symbols))

#pass1 =''.join(password)
#print(password)
#print(pass1)


    