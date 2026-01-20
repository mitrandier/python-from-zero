height = float(input("Hi, please enter your height in m: "))
weight = int(input("and please enter your weight in kg :"))
bmi    = round( weight / (height**2), 2)

if   bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")

#print ( bmi )
#print(round (weight / (height**2) , 2))

      