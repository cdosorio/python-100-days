import os
from twilio.rest import Client
import smtplib

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "cdosorio@gmail.com"
PASSWORD = "1234"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        pass

    def send_SMS(self, msg):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
               
        message = client.messages \
                        .create(
                            body=msg,
                            from_='+17473024549',
                            to='+56977964322'
                        )

        print(message.status)

    def send_email(self, to_address, subject, body, google_flight_link):
        print("Sending email...")
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls() #encrypt message
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=to_address, 
                msg=f"Subject:{subject}\n\n{body}\n{google_flight_link}".encode('utf-8')
                )