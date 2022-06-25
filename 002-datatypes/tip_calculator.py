print("Welcome to the tip calculator!")
total_bill = round(float(input("What was the total bill?")), 2)
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
total_people = int(input("How many people to split the bill?"))

bill_per_person = round((total_bill * (1 + tip/100)) / total_people, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${ final_amount}")