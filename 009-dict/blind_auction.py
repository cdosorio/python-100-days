import os
clear = lambda: os.system('cls')

from art import *

print(logo)
bids = {}
should_continue = True

while should_continue:
    name = input("Please indicate your name... ")
    price = int(input("Please indicate your bid... "))
    bids[name] = price
    should_continue = (input("Please indicate if there are other bids (Yes or No)\n").lower() == "yes")
    if should_continue:
        clear()

max_bid = 0
winner_name = ""
for key in bids:
    if bids[key] > max_bid:
        max_bid = bids[key]
        winner_name = key

print(f"The winner is {winner_name} with a bid of {max_bid}")

