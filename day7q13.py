# Write a program to input a year and check whether it is a leap year or not using conditional statements.
year=int(input("Enter year:"))
if (year%400==0) :
    print("Non leap year")
elif year%4==0 and year%100!=0:
    print("Leap year")
else:
    print("Non leap year")
