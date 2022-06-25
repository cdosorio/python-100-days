from fcntl import F_FULLFSYNC
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

should_continue = True

while should_continue:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        should_continue = False
        continue
    if choice == "report":
        coffee_maker.report()
        money_machine.report234()
        continue
    
    drink = menu.find_drink(choice)
    if not drink:
        continue
    if not coffee_maker.is_resource_sufficient(drink):
        continue    
    if not money_machine.make_payment(drink.cost):
        continue
    coffee_maker.make_coffee(drink)