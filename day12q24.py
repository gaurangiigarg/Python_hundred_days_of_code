"""Write a program to calculate electricity bill based on units consumed with these rates: 
First 100 units at ₹5/unit 
Next 100 units at ₹7/unit 
Next 100 units at ₹10/unit 
Above at ₹12/unit"""
unit=int(input("Enter number of units:"))
if unit<=100:
    print("Electricity bills is ",unit*5)
elif unit<=200:
    print("Electricity bills is ",500+(unit-100)*7)
elif unit<=300:
    print("Electricity bills is ",1200+(unit-200)*10)
else:
    print("Electricity bills is ",5*100+7*100+100*10+(unit-300)*12)
