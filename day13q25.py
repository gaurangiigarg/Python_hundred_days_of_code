# Write a program to implement a basic calculator using switch-case for +, -, *, /, %.
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
op=input("Choose (+,-,*,/,%):")[0]
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    if num2==0:
        print("Division by zero is not handled")
    else:
        print(num1/num2)
elif op=="%":
    print(int(num1)%int(num2))
else:
    print("Invalid operator")