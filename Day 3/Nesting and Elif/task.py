print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age?"))
    if age <= 16:
        print("Your ticket price is 400 rupees")
    elif age <= 18:
        print("Your ticket price is 600 rupees")
    else:
        print("Your ticket price is 800 rupees")




else:
    print("Sorry you have to grow taller before you can ride.")
