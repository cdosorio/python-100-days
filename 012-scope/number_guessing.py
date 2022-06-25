import random

EASY_TURNS = 5
HARD_TURNS = 10

print("Welcome to the number guessing game")
print("I'm thinking in a number betwenn 1 and 100")
choosen_number = random.randint(1, 100)

dificulty = input("Choose a dificulty. Type 'easy' or 'hard': ")
attempts = EASY_TURNS
if dificulty == 'hard':
    attempts = HARD_TURNS

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess")
    guess = int(input("Make a guess: "))
    if guess == choosen_number:
        print ("You win!!")
        attempts = 0
    else:
        attempts -= 1
        if attempts == 0:
            print(f"You loose. Number is {choosen_number}")
        if guess > choosen_number:
            print("Too high")        
        elif guess < choosen_number:
            print("Too low")           
