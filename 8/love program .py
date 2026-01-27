name1 = input("Hi, please enter the first person name:")
name2 = input("Hi, please enter the second person name:")
name3 = name1+ name2
name4 = name3.lower()
print(name4,type(name4))

true=0
love=0

a=name4.count("t")
b=name4.count("r")
c=name4.count("u")
d=name4.count("e")
count_true = a+b+c+d
print("Total_true:",count_true)

e=name4.count("l")
f=name4.count("o")
g=name4.count("v")
h=name4.count("e")
count_love = e+f+g+h
print("Total_love:",count_love)

final_result=(count_true*10) + count_love
if final_result <= 10 or final_result >= 90:
    print(f"your score is {final_result}, you go together like coke and mentos.")
elif final_result >= 40 and final_result <= 50:
    print(f"your score is {final_result}, you are alright together.")
else:
    print(f"Your score is {final_result}.")
    
