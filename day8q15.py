# Write a program to input a character and check whether it is an uppercase alphabet, lowercase alphabet, digit, or special character.
ch=input("Enter a character:")[0]
if ch.isupper():
    print("Uppercase alphabet")
elif ch.islower():
    print("Lowercase alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")