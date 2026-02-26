# Write a program to print the product of even numbers from 1 to n.
n = int(input("Enter a number:"))
if n==1:
    print("No even numbers to multiply")
else:
    prod=1
    for i in range(2,n+1,2):
        prod*=i
    print("Product is",prod)