# Write a program to find the HCF (GCD) of two numbers.
import math
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
hcf=math.gcd(num1,num2)
print(f"HCF of {num1} and {num2} is {hcf}")
