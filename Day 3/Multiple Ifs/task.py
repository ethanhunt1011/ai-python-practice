print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child pay $5.")
    elif age <= 18:
         bill =7
         print("Youth pay $7.")
    else:
        bill = 12
        print("Adult pay $12.")
    photo = input("Do you need a photo if Yes type Y , No type N : ").lower()
    if photo == "y":
        bill+=3
        print(f"Your ticket price is : {bill}$ ")
    elif photo =="n":
        print(f"Your ticket price is : {bill}$")
    else:
        print("Wrong input try again")


else:
    print("Sorry you have to grow taller before you can ride.")
