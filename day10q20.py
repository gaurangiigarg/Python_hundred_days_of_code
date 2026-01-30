# Write a program to display the day of the week based on a number (1–7) using switch-case.
n=int(input("Enter your choice(1-7):"))
if n==1:
    print("Monday")
elif n==2:
    print("Tuesday")
elif n==3:
    print("Wednesday")
elif n==4:
    print("Thursday")
elif n==5:
    print("Friday")
elif n==6:
    print("Saturday")
elif n==7:
    print("Sunday")
else:
    print("Invalid choice")