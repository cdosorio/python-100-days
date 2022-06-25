##################### Hard Starting Project ######################
import random
import smtplib
import pandas
import datetime as dt
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

my_email = "cdosorio@gmail.com"
password = "1234"

def send_email(to_address, subject, body):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #encrypt message
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=to_address, 
            msg=f"Subject:{subject}\n\n{body}")

df = pandas.read_csv("birthdays.csv")
df = df.set_index(['month', 'day']) #use 2-columns as key
dict = df.to_dict("index") # Turn into dict
#dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.items} # using comprehension
print(dict)

now = dt.datetime.now()
today_tuple = (now.month, now.day)

if today_tuple in dict:
    print("found ")
    data = dict[today_tuple]

    # prepare and send letter
    letter_number = random.randint(1,3)
    with open(f"./letter_templates/letter_{letter_number}.txt") as file:
        letter = file.read()
        new_letter = letter.replace("[NAME]", data["name"])
        send_email(data["email"], "Happy birtday", new_letter)
else:
    print("not found a birthday")






