# Write a program to check if a number is an Armstrong number.
n=int(input("Enter a number:"))
digit=len(str(n))
s=0
for i in str(n):
    s+=int(i)**digit
if n==s:
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")