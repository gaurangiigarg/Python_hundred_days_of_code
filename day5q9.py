# Write a program to calculate simple and compound interest for given principal, rate, and time.
p=float(input("Enter the principal amount(in rupees):"))
r=float(input("Enter rate(in %):"))
t=float(input("Enter time(in years):"))
print("Simple interest is:",(p*r*t)/100)
print("Compound interest is:",(p* (1+r/100)** t-p))
