import random
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
selection = int(input("What do you choose? Type 0 for rock , 1 for paper and 2 for scissors.\n"))
computer_selection = random.randint(0,2)
if selection == 0 and computer_selection ==1:
    print(f"You choose - {selection}{rock}\n Computer choose -{computer_selection} {paper}\n You Lose")
elif selection    == 1 and computer_selection == 0:
    print(f"You choose - {selection}{paper}\n Computer choose - {computer_selection}{rock}\n YOU WIN")
elif selection == 2 and computer_selection   == 0:
    print(f"You choose = {selection}{scissors}\n Computer choose = {computer_selection}{rock}\n YOU Lose")
elif selection == 0 and computer_selection   == 2:
    print(f"You choose = {selection}{rock}\n Computer choose = {computer_selection}{scissors}\n YOU WIN ")
elif selection == 1 and computer_selection   == 2:
    print(f"You choose ={selection} {paper}\n Computer choose = {computer_selection}{scissors}\n You Lose")
elif selection == 2 and computer_selection   == 1:
    print(f"You choose = {selection}{scissors}\n Computer choose = {computer_selection}{paper}\n You win ")
elif selection == 0 and computer_selection   == 0:
    print(f"You and Computer choose - {rock}\n SO ITS A TIE ")
elif selection == 1 and computer_selection   == 1:
    print(f"You and Computer choose - {paper}\n SO ITS A TIE ")
elif selection == 2 and computer_selection   == 2:
    print(f"You and Computer choose - {scissors}\n SO ITS A TIE ")
else:
    print("Wrong input , Please try again.")