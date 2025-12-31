#a = -5
#b = 4
#c = 9
#m = a
#if b < m:
#    m = b
#if c < m:
#    m = c
#print("the lowest number is:", m )

#A = [7, 12, 9, 14, 15, 8]
#print("A=", A)
#print(A)
#print(A[0])
#for i in range (7):
#    print("Element" , i , "of A is:  " , A[i])
    
    
def manfi(x):
    return -x
w= manfi(5)+manfi(6)
print(w)



def Min(A):
    m = A[0]
    for i in range (1,len(A)):
        if m > A[i]:
            m = A[i] 
    return m
A = [7, 12, 9, 14, 15, 8, 1, 3, 66, 78, 800]
print(len (A))
x= Min(A)
print(x)
        