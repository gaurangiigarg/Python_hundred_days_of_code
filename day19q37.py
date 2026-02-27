#Write a program to find the LCM of two numbers.
import math
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if num1==0 or num2==0:
    print("LCM is 0")
else:
    hcf=math.gcd(num1,num2)
    lcm=(num1*num2)//hcf
    print(f"LCM of {num1} and {num2} is {lcm}")