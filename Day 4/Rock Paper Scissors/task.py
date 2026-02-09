import random
from math import radians

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
gamelist = [rock,paper,scissors]
user_choice = int(input("Hello welcome to the game . \n select 0 for rock  1 for paper and 2 for scissors:\n"))


if 0<=user_choice<=3:
    print(f"You choose {gamelist[user_choice]} ")
computer = random.randint(0,2)
print(f"computer choose {gamelist[computer]}")

if 0>user_choice>=3:
    print("You have entered wrong , YOU LOST.")

elif user_choice==computer:
    print("ITS A TIE")

elif user_choice == 2 and computer ==0:
     print("You lose")
elif computer == 2 and user_choice==0:
     print("You win")
elif user_choice>computer:
    print("You win")
elif user_choice<computer:
    print("You lose")
