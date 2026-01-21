print("Hello, wellcome to our ticket market")
height = int(input("please enter your height in cm: "))

bill = 0
if height >= 110:
    age = int(input(" please enter your age: "))
    if age <= 13:
        print("child tickets are 5$")
        bill = 5
    elif age <= 19:
        print("young tickets are 7$")
        bill = 7
    else:
        print("adult tickets are 12$")
        bill = 12
            
    photo = input("do you want take photos? please answer by y and n : ")
    if photo == "y":
        bill += 3
        
    print(f"your final ticket is equal: {bill}$. have fun!")
    
    
else:
    print("sorry, you have to grow taller befor you can ride.")




    