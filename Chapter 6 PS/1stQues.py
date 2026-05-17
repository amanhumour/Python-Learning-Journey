a = int(input("Enter the 1st number: "))
a2 = int(input("Enter the 2nd number: "))
a3 = int(input("Enter the 3rd number: "))
a4 = int(input("Enter the 4th number: "))

if a > a2 and a > a3 and a > a4:
    print("The greatest number is: ", a)
elif a2 > a3 and a2 > a4:
    print("The greatest number is: ", a2)
elif a3 > a4:
    print("The greatest number is: ", a3)
else:
    print("The greatest number is: ", a4)   


