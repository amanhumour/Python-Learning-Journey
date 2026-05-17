a = int(input("Enter your age: "))
#if elif else ladder
#if statement no. 1
if(a%2==0):
    print("a is even")
#statement 1 ends here    

#if statement no. 2
if(a>=18):
    print("You are above the age of consent")

elif(a<0):
    print("You are entering wrong age")

elif(a==0):
    print("You are entering 0 which is not a valid age")    

else:
    print("You are below the age of consent")

#statement 2 ends here    

print("End of program")

#There can be any number of Elif statements.
# Last else is executed only if all the conditions inside Elifs fail.

