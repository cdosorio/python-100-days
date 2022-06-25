import smtplib

my_email = "cdosorio@gmail.com"
password = "1234"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #encrypt message
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="cdosorio@outlook.com", 
        msg="Subject:Hello\n\nThis is the body")

