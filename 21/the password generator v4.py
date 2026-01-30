import random
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
          'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
numbers=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols=['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']

print("Welcome to the Pypassword Generator!")
letters_num = int(input("How many letters would you like in your password?\n"))
number_num= int(input("How many numbers would you like?\n"))
symbols_num= int(input("How many symbols would you like?\n"))
#Hard level
password_list = []
for char in range(1, letters_num + 1):
    #password_list += random.choice(letters)
    password_list.append(random.choice(letters))
    print(password_list)

for char in range(1, number_num + 1):
    #password_list += random.choice(numbers)
    password_list.append(random.choice(numbers))
    print(password_list)

for char in range(1, symbols_num + 1):
    #password_list += random.choice(symbols)
    password_list.append(random.choice(symbols))
    print(password_list)
    
print("\n")
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print("your password is: ", password)






# password = ""
# 
# for char in range(1, letters_num + 1):
#     password += random.choice(letters)
#     print(password)
# 
# for char in range(1, number_num + 1):
#     password += random.choice(numbers)
#     print(password)
# 
# for char in range(1, symbols_num + 1):
#     password += random.choice(symbols)
#     print(password)


# password = []
# for i in range (0,letters_num):
#     password.append(random.choice(letters))
# for i in range (0,number_num):
#     password.append(random.choice(numbers))
# for i in range (0,symbols_num):
#     password.append(random.choice(symbols))
# 
# final_pass =''.join(password)
# #print(password)
# print(f'Your secure password is: {final_pass} ')
    

    
