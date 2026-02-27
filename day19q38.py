# Write a program to find the sum of digits of a number.
n=int(input("Enter a number:"))
a=str(n)
sum=0
for i in a:
    sum+=int(i)
print(f"The sum of digits of {n} is {sum}")