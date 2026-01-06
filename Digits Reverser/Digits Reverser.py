a = int(input())

b = a%10

c =(a//10)%10

d = (a//100)%10

e = a//1000

b ,c ,d ,e = str(b) ,str(c) ,str(d) ,str(e)

print( e+b+c+d)