a = int(input("Enter the 1st subject marks: "))
a2 = int(input("Enter the 2nd subject marks: "))
a3 = int(input("Enter the 3rd subject marks: "))
# 33 from 100 is the passing marks for each subject. The total marks for all three subjects is 300. To pass with distinction, the total marks should be 120 or above.

total_percentage = (a + a2 + a3) / 300 * 100

if total_percentage >= 40 and a >= 33 and a2 >= 33 and a3 >= 33:
    print("Congratulations! You have passed with distinction.", total_percentage)
else:
    print("You are Failed.", total_percentage)    



    
