def in_to_cm(inches):
    return inches * 2.54    

inches = float(input("Enter the length in inches: "))
print("The length in centimeters is: ", round(in_to_cm(inches), 2))