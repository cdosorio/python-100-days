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

#Write your code below this line 👇
game_images = [rock, paper, scissors]

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

if (human_choice > len(game_images) or human_choice < 0):
    print("Invalid number")
else:    
    if (human_choice == computer_choice):
        print("Draw")
    elif ((human_choice == 0 and computer_choice == 2) or (human_choice == 2 and computer_choice == 1) or (human_choice == 1 and computer_choice == 0)):
        print("You win")
    else:
        print("Computer win")

    print(f"Your choice:\n {game_images[human_choice]} . \n\nComputer choice:\n {game_images[computer_choice]}")


