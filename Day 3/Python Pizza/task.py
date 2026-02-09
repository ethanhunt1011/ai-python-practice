print("Welcome to Python Pizza")

size = input("What size pizza do you want , S , M or L: ").lower()


bill = 0
if size== "s":
    bill+=15
    pepperoni = input("Do you need pepperoni , Y or N : ").lower()
    if pepperoni == "y":
        bill += 2
    extra_cheese = input("Do you need extra cheese , Y or N : ").lower()
    if extra_cheese == "y":
            bill += 1
    print(f"Your final bill : {bill}")

elif size =="m":
    bill+=20
    pepperoni = input("Do you need pepperoni , Y or N : ").lower()
    if pepperoni == "y":
        bill += 3
    extra_cheese = input("Do you need extra cheese , Y or N : ").lower()
    if extra_cheese == "y":
            bill += 1
    print(f"Your final bill : {bill}")
elif size=="l":
    bill+=25
    pepperoni = input("Do you need pepperoni , Y or N : ").lower()
    if pepperoni == "y":
        bill += 3
    extra_cheese = input("Do you need extra cheese , Y or N : ").lower()
    if extra_cheese == "y":
            bill += 1
    print(f"Your final bill : {bill}")
else:
    print("wrong input try again")









