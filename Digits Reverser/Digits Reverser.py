a = int(input())
print(a)

b = a%10
print(b)

c =(a//10)%10
print(c)

d = (a//100)%10
print(d)

e = a//1000
print(e)

b ,c ,d ,e = str(b) ,str(c) ,str(d) ,str(e)

print(e+b+c+d)

