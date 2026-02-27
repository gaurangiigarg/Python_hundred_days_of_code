n=int(input("Enter a number:"))
a=str(n)
b=a[::-1]
if a==b:
    print(f"{n} is pallindrome number")
else:
    print(f"{n} is not a pallindrome number")