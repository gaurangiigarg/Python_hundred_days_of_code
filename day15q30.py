# Write a program to reverse a given number.
no=int(input("Enter a number:"))
if no>0:
    n=str(no)
    rev=n[::-1]
    print(rev)
else:
    no=-no
    n=str(no)
    rev=n[::-1]
    print("-"+rev)