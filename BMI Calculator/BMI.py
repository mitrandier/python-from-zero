print("please enter your Height and weight:")
h, w = input().split() 
h= int(h)
h=h/100
h=h*h
w=int(w) 
bmi=w/h
print(bmi)