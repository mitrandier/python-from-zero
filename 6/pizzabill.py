size = input("Hi, wich type of pizza do you want to order? Small, Medium or Large?")
bill = 0
if  size== "s":
    bill+=15
elif size=="m":
    bill +=20
elif size=="l":
    bill +=25
    
peperoni = input("do you want extra peperoni? y or n ?")
if peperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

cheese = input("do you want some extra cheese on your pizza ? y or n ?")
if cheese == "y":
    bill += 1

print(f"your final bill is: ${bill}")