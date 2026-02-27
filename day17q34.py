#Write a program to check if a number is prime.
n=int(input("Enter a number:"))
if n<=1:
    print(f"{n} is not a prime number")
else:
    a=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            a=False
            break
    if a:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")