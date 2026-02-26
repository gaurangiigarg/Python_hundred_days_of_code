"""Write a program to calculate library fine based on late days as follows: 
First 5 days late: ₹2/day 
Next 5 days late: ₹4/day 
Next 20 days days late: ₹6/day 
More than 30 days: Membership Cancelled."""
day=int(input("Enter the days:"))
if day<=5:
    print("Fine =",day*2)
elif day<=10:
    print("Fine =",5*2+(day-5)*4)
elif day<=30:
    print("Fine =",30+(day-10)*6)
else:
    print("Membership cancelled")
