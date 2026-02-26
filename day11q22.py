# Write a program to find profit or loss percentage given cost price and selling price.
cp=float(input("Enter cost price:"))
sp=float(input("Enter selling price:"))
if(cp < sp):
    print("Profit Percentage:",((sp-cp)/cp)*100)
elif(cp > sp):
    print("Loss Percentage:",((cp-sp)/cp)*100)
else:
    print("No loss, No Profit")