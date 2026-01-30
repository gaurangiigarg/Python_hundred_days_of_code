# Write a program to input a character and check whether it is a vowel or consonant using if–else.
ch=input("Enter a character:")[0]
if ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")