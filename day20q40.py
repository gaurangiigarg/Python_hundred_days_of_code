# Write a program to find the 1’s complement of a binary number and print it.
binary=input("Enter a binary number:")
s=""
for i in binary:
    if i=='0':
        s+='1'
    else:
        s+='0'
print(f"The 1's complement of {binary} is {s}")