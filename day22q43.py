#Write a program to check if a number is a strong number.
import math
n=int(input("Enter a number:"))
no=str(n)
sum=0
for i in no:
    digit=int(i)
    sum+=math.factorial(digit)
if sum==n:
    print(f"{n} is a strong number")
else:
    print(f"{n} is not a strong number")
