# factorial(1) = 1
# factorial(2) = 2 X 1
# factorial(3) = 3 X 2 X 1
# factorial(4) = 4 X 3 X 2 X 1
# factorial(5) = 5 × 4 X 3 X 2 X 1

# factorial(n) = n X n-1 x ...... 3 X 2 X1

# factorial(n) = n * factorial(n-1)

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter the number: "))    
print("The factorial of", n, "is", factorial(n))
