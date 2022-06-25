from data import *
e
def print_report():
    for key in resources:
        print(f"{key} : {resources[key]}")

def check_resources(choice):
    ingredients = MENU[choice]["ingredients"]
    for key in ingredients:
        if  ingredients[key] > resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    
    return True

def check_coins(choice):
    global profit
    profit = 0

    cost = MENU[choice]["cost"]
    print(f"Please insert {cost}")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    money_inserted = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    charge = money_inserted -  MENU[choice]["cost"]

    if charge < 0:
        print(f"Sorry that's not enough money. Money refunded")
        return False
    elif charge > 0:
        print(f"You inserted {money_inserted}. Here is ${round(charge,2)} dollars in change")
        profit = MENU[choice]["cost"]
        update_money()
    
    return True

def update_money():
    global profit
    #print(f"Adding {profit} to money")
    if not "money" in resources.keys():
        resources["money"] = profit
    else:
        resources["money"] += profit

def update_resources(choice):
    ingredients = MENU[choice]["ingredients"]
    for key in ingredients:
        resources[key] -= ingredients[key]
    
profit = 0
should_continue = True

while should_continue:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        should_continue = False
        continue
    if choice == "report":
        print_report()
        continue
    if not choice in MENU.keys():
        print("Not found")
        continue

    if not check_resources(choice):
        continue

    if not check_coins(choice):
        continue
    
    update_resources(choice)

    print(f"Here is your {choice}. Enjoy!")


    