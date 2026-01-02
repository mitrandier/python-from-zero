

print(" hi,today we want to make a digital hour :) ")
while True:
    try:
        hour = int(input("please enter the hour: "))
        if 0 <= hour <= 23:
            break
        else:
            print("number must be between 0 - 24")
    except ValueError:
        print("please enter the number no character!")


while True:
    try:
        minute = int(input("please enter the minute:  "))
        if 0 <= minute <= 59:
            break
        else:
            print("number must be between (0-59)")
    except ValueError:
        print("please enter the number no character!")


while True:
    try:
        second = int(input("please enter the second: "))
        if 0 <= second <= 59:
            break
        else:
            print("number must be between (0-59)")
    except ValueError:
        print("please enter the number no character!")


print(hour ,":", minute ,":", second)
