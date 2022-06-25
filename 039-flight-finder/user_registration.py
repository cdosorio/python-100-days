from data_manager import DataManager

data_manager = DataManager()

print('''
Welcome to Angela's flight Club
We find the best deals
''')
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
email_check = input("Type your email again\n")

while email != email_check:
    print("Emails are not the same")
    email = input("What is your email?\n")
    email_check = input("Type your email again\n")
else:
    data_manager.create_user(first_name, last_name, email)
    print("You are in the club!")






