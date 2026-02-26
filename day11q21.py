# Write a program to display the month name and number of days using switch-case for a given month number.
# Write a program to display the day of the week based on a number (1–7) using switch-case.
n=int(input("Enter your choice(1-12):"))
if n==1:
    print("January-31 days")
elif n==2:
    print("February-28 days")
elif n==3:
    print("March-31 days")
elif n==4:
    print("April-30 days")
elif n==5:
    print("May-31 days")
elif n==6:
    print("June-30 days")
elif n==7:
    print("July-31 days")
elif n==8:
    print("August-31 days")
elif n==9:
    print("September-30 days")
elif n==10:
    print("October-31 days")
elif n==11:
    print("November-30 days")
elif n==12:
    print("December-31 days")
else:
    print("Invalid choice")