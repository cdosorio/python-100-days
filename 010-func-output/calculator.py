import os
clear = lambda: os.system('cls')

from art import *

print(logo)

def add(a,b):
    return a+b
    
def substract(a,b):
    return a - b
    
def multiply(a,b):
    return a * b
    
def divide(a,b):
    return a/b

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide 
    }

def calculator():
    should_continue = True
    result = ""

    while should_continue:
        if result == "":
            a = float(input("Please indicate first number... "))
        else:
            a = result
        for key in operations:
            print(key)
        operation = input("Pick operation... ")
        b = float(input("Please indicate second number... "))

        result = operations[operation](a,b)
        print(f"{a}{key}{b} = {result}")

        should_continue = input("Please indicate y to continue calculatio with {result} or type n to start new calculation \n").lower() == "y"
        if not should_continue:            
            clear()
            calculator()    

calculator()