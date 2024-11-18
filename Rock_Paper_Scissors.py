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
###########################################################################
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

computer_choice = random.randint(0,2)


if user_choice == 0:
    print(rock , "ROCK")
elif user_choice == 1:
    print(paper , "PAPER")
elif user_choice == 2:
    print(scissors, "SCISSORS")
else:
    print("NOT A VALID CHOICE!")


if computer_choice == 0:
    print(f"Computer chose\n ROCK", rock)
elif computer_choice == 1:
    print(f"Computer chose\n PAPER", paper)
elif computer_choice == 2:
    print(f"Computer chose\n SCISSORS", scissors)
else:
    print("This shouldnt print")


if user_choice == 0 and computer_choice == 0:
    print("TIE!")
elif user_choice == 0 and computer_choice == 1:
    print("YOU LOSE!")
elif user_choice == 0 and computer_choice == 2:
    print("YOU WIN!")
elif user_choice == 1 and computer_choice == 0:
    print("YOU WIN!")
elif user_choice == 1 and computer_choice == 1:
    print("TIE!")
elif user_choice == 1 and computer_choice == 2:
    print("YOU LOSE!")
###
elif user_choice == 2 and computer_choice == 0:
    print("YOU LOSE!")
elif user_choice == 2 and computer_choice == 1:
    print("YOU WIN!")
elif user_choice == 2 and computer_choice == 2:
    print("TIE!")
else:
    print("This shouldnt print")