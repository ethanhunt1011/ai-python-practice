print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("Yes you can ride")
    age = int(input("Please enter your age: "))
    if age > 18:
        print("You have to pay 12$")
    elif 12<=age<=18 :
        print("You have to pay 7$ ")
    else:
        print("Please pay 5$")
else:
    print("Sorry you cant ride")






