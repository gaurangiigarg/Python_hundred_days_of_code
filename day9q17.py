# Write a program to find the roots of a quadratic equation and categorize them.
import math
print("The given equation is: ax^2+bx+c")
a=int(input("Enter the coefficient of a:"))
b=int(input("Enter the coefficient of b:"))
c=int(input("Enter the coefficient of c:"))
D=(b*b)-(4*a*c)
if D>0:
    x1=(-b+ math.sqrt(D))/(2*a)
    x2=(-b-math.sqrt(D))/(2*a)
    print("Roots are real and distinct")
    print("The roots of equation is",x1,"and",x2)
elif D==0:
    x=(-b)/(2*a)
    print("Roots are real and equal")
    print("The roots of equation is",x)
else:
    print("Roots are imaginary")