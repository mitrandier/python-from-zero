print("Hello, wellcome to our ticket market")
height = int(input("please enter your height in cm: "))

bill = 0
if height >= 110:
    age = int(input(" please enter your age: "))
    if age <= 13:
        bill = 5
        print("child tickets are $5.")
    elif age <= 19:
        bill = 7
        print("young tickets are $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("your entery ticket price is free .")
        print("everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("adult tickets are $12.")
        
            
    photo = input("do you want take photos? please answer by y and n : ")
    if photo == "y":
        bill += 3
        
    print(f"your final ticket is equal: {bill}$. have fun!")
    
    
else:
    print("sorry, you have to grow taller befor you can ride.")