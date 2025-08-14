print("Welcome to Python Pizza Deliveries!")
size = input("Which pizza would you like to order ? S , M or L")
pepperoni = input("Do you want pepporoni for your order ? Write Y for yes and N for no")
extra_cheese = input("Do you want extra cheese for your Pizza ,Y or N?")
bill = 0


if size =="S":
    bill = 15
    if pepperoni == "Y":
        bill +=2
    if extra_cheese == "Y":
       bill += 1
    print(f"Your final bill is: ${bill}.")
elif size == "M":
     bill = 20
     if pepperoni == "Y":
        bill += 3
     if extra_cheese == "Y":
        bill += 1
     print(f"Your final bill is: ${bill}.")
elif size == "L":
     bill = 25
     if pepperoni == "Y":
        bill += 3
     if extra_cheese == "Y":
        bill += 1
     print(f"Your final bill is: ${bill}.")
else:
    print("You have entered a wrong keyword!!")




