# Write a program to find the product of odd digits of a number.
n=int(input("Enter a number:"))
prod=1
a=str(n)
for i in a:
    digit=int(i)
    if digit%2!=0:
        prod*=digit
print(f"The product of odd digits of {n} is {prod}")