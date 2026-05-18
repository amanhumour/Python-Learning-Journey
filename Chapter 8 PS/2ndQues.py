def f_to_c(f):
    c = (f - 32) * 5.0/9.0
    return c

f = int(input("Enter the temperature in Fahrenheit: "))
print("The temperature in Celsius is: ", round(f_to_c(f), 2))   