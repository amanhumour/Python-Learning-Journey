# 5! = 5*4*3*2*1 = 120 factorial of 5 is 120

n = int(input("Enter the number: "))

product = 1
for i in range(1, n+1):
    product *= i

print(f"The factorial of {n} is {product}.")