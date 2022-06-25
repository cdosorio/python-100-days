#import math
import smtplib
import requests
from datetime import datetime, timezone
import time

MY_LAT = -31.448891 
MY_LONG = -72.669266 
MAX_DIFF = 5

my_email = "cdosorio@gmail.com"
password = "1234"

# ---------------------------- FNS ------------------------------- #
def check_over_head(iss_latitude, iss_longitude):
    return (abs(MY_LAT - iss_latitude) < MAX_DIFF or abs(MY_LONG - iss_longitude) < MAX_DIFF)

def send_email(to_address, subject, body):
    print("Sending email...")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #encrypt message
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=to_address, 
            msg=f"Subject:{subject}\n\n{body}")

def check_is_dark(sunrise, sunset, now):
    return now >= sunset and now < sunrise

# ---------------------------- MAIN LOGIC SETUP ------------------------------- #
while True:
    time.sleep(60) #simple timer
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    is_over_head = True;#check_over_head(iss_latitude, iss_longitude)
    print(f"is_over_head: {is_over_head}")

    if is_over_head:
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()

        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now(timezone.utc)

        #If the ISS is close to my current position
        # and it is currently dark
        # Then send me an email to tell me to look up.
        # BONUS: run the code every 60 seconds.
        is_dark = check_is_dark(sunrise, sunset, time_now.hour)
        print(f"sunrise:{sunrise}, sunset: {sunset}, now:{time_now.hour}  is_dark: {is_dark}")

        if is_dark:
            send_email("cdosorio@outlook.com", "IIS over head", "IIS is over head now!")






