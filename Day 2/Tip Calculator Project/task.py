#
print("Welcome to the tip calculator")
bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage would you like to offer? 10,12,15\n"))
people = int(input("How many people to split the bill?\n"))
final_bill = round(bill*(tip/100)/people , 2)
print(f"Each person should pay: {final_bill}")