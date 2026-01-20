year = int(input("please enter the year: "))

four = year % 4
hundred = year % 100
four_hundred = year % 400

if four == 0:
    if hundred == 0:
        if four_hundred == 0:
            print("this year is a leap year")
        else:
            print("this year isnt a leap year")
    else:
        print("this year is a leap year")
else:
    print("this year isnt leap year")