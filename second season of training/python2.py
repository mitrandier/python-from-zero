#print("Hi please enter your number:")
#n = int(input())
#x = 1
#for i in range(n):
#    print("i=", i+1)
#    x= x * (i+1) 
#    print("x=", x)
#    print(n , "!=" , x)
    
    
print("Hi please enter your number:")
n = int(input())
s = 0
for i in range (1,n+1):
    s = s + i
    print(s)
    print ("the sum of 1 to", n , "is : " , s)