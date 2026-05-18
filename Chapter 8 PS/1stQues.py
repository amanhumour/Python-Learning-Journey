def Biggest(a, b, c):
 
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
a =1
b=4
c=9

print("The biggest number is: ", Biggest(a,b,c))