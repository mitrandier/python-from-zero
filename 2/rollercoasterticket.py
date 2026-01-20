print("Hello, wellcome to our ticket market")
height = int(input("please enter your height in cm: "))

if height >= 110:
    age = int(input(" please enter your age: "))
    if age <= 13:
        print("please pay 5$ ")
    elif age <= 19:
        print("please pay 7$ ")
    else:
        print("please pay 12$")
else:
    print("sorry, you have to grow taller befor you can ride.")

