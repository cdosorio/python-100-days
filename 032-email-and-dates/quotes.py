import random
import smtplib
import datetime as dt

my_email = "cdosorio@gmail.com"
password = "1234"

def send_email(subject, body):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #encrypt message
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="cdosorio@outlook.com", 
            msg=f"Subject:{subject}\n\n{body}")


now = dt.datetime.now()
day_of_week = now.weekday()
#print(day_of_week)
if day_of_week == 0: # monday
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        quote = random.choice(quotes)
        send_email("Quote for monday", quote)

    