# Write a program to swap two numbers without using a third variable.
num1=int(input("Enter first number:\n"))
num2=int(input("Enter second number:\n"))
print("Before swapping:")
print("First number is:",num1)
print("Second number is:",num2)
num1,num2=num2,num1
print("\nAfter swapping:")
print("First number is:",num1)
print("Second number is:",num2)