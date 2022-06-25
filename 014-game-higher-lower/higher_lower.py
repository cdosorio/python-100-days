import os
import random
clear = lambda: os.system('cls')

from game_data import *
from art import *

def compare(guess, a, b):
    if (a["follower_count"] > b["follower_count"] ):
        return guess == "a"
    else:
        return guess == "b"

continue_game = True
score = 0
b =  random.choice(data)
        
print("HIGER LOWER GAME")
while continue_game:
    #clear()          
    a = b
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    
    print(f'Compare A: {a["name"]} a {a["description"]}, from {a["country"]}  ')
    print("VS")
    print(f'Against B: {b["name"]} a {b["description"]}, from {b["country"]}  ')
    guess = input(f"Who has more followers? Type 'a' or 'b': ")
    
    if compare(guess, a,b):
        score += 1
        print(f'You are right!. {a["follower_count"]} VS {b["follower_count"]} Current score: {score}\n')        
    else:
        print(f'You are wrong!. {a["follower_count"]} VS {b["follower_count"]} Final score: {score}\n')
        continue_game = False
    

    
