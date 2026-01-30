""" Write a program that accepts a percentage (0-100) and assigns a grade based on the following criteria: 
90-100: Grade A 
80-89: Grade B 
70-79: Grade C 
60-69: Grade D 
below 60: Grade F. """
marks=float(input("Enter percentage:"))
if marks<=100 and marks>=90:
    print("Grade A")
elif marks<=89 and marks>=80:
    print("Grade B")
elif marks<=79 and marks>=70:
    print("Grade C")
elif marks<=69 and marks>=60:
    print("Grade D")
else:
    print("Grade F")