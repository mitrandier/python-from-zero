num = int(input("hi enter your number: "))

def isitprime(number):
    check = 0
    test = True
    for i in range(2,number):
        check = number % i
        if check == 0:
            test = False
            #print(f"no this number isn't prime")
    if test == False:
        print(f" {number} isn't prime")
    else:
        print(f"Yes {number} is prime")
 
    



isitprime(num)

