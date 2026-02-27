#Write a program to take a number as input and print its equivalent binary representation.
n=int(input("Enter a number:"))
a=bin(n)[2:]
print(f"Binary of {n} is {a}")
