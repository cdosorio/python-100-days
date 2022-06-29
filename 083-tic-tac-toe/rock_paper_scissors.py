import random
from enum import Enum

# Enum support from 3.4
class Choices(Enum):
    PIEDRA = 1
    PAPEL = 2
    TIJERAS = 3

def play():
    user_choice = Choices[input("Choose: PIEDRA PAPEL TIJERAS ").upper()]
    program_choice = Choices(random.randint(1, 3))

    print(f"user_choice: {user_choice.name} program_choice: {program_choice.name}")
    
    if user_choice ==  program_choice:
        print("Tie!")
    elif (user_choice == Choices.PIEDRA and program_choice == Choices.TIJERAS or 
        user_choice == Choices.PAPEL and program_choice == Choices.PIEDRA or 
        user_choice == Choices.TIJERAS and program_choice == Choices.PAPEL):
        print("You win!")
    else:
        print("You lost!")

play()


