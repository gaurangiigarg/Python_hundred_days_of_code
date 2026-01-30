# Write a program to classify a triangle as Equilateral, Isosceles, or Scalene based on its side lengths.
side1=int(input("Enter first side of triangle:"))
side2=int(input("Enter second side of triangle:"))
side3=int(input("Enter third side of triangle:"))
if side1+side2>side3 and side2+side3>side1 and side1+side3>side2:
    if side1==side2 and side2==side3 and side3==side1:
        print("Equilateral Triangle")
    elif side2==side1 or side1==side3 or side2==side3:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid Triangle")